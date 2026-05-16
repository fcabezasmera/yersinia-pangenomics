library(caper)
library(ape)

cat("=== D Statistic Analysis — Yersinia AMR traits ===\n\n")

# Load tree (rpoB full, 9957 tips)
cat("Loading tree...\n")
tree <- read.tree("10_gwas/rpoB_tree_scoary2.nwk")
cat("Tips:", length(tree$tip.label), "\n")

# Load traits
cat("Loading traits...\n")
traits <- read.csv("11_phylo_stats/d_statistic_traits.csv", stringsAsFactors=FALSE)
cat("Traits:", nrow(traits), "genomes x", ncol(traits), "columns\n\n")

# Make tree ultrametric (required by caper)
cat("Making tree ultrametric...\n")
tree_ultra <- chronos(tree, quiet=TRUE)

# Match tips to traits
traits_matched <- traits[traits$accession %in% tree_ultra$tip.label, ]
rownames(traits_matched) <- traits_matched$accession
cat("Matched:", nrow(traits_matched), "genomes\n\n")

# Create comparative data object
comp_data <- comparative.data(
    phy  = tree_ultra,
    data = traits_matched,
    names.col = "accession",
    warn.dropped = FALSE
)

# Define traits to test
traits_to_test <- c(
    # One Health niches
    "niche_H", "niche_A", "niche_F", "niche_E",
    # Key AMR genes from GWAS
    "amr_blaA", "amr_vat_F_", "amr_blaYRC",
    "amr_tet_A_", "amr_sul2", "amr_sul1",
    "amr_aadA1", "amr_aadA12", "amr_floR",
    "amr_sat2", "amr_dfrA1", "amr_qacEdelta1",
    # Plasmid
    "has_plasmid"
)

# Filter to traits present in data
traits_to_test <- traits_to_test[traits_to_test %in% colnames(traits_matched)]
cat("Testing", length(traits_to_test), "traits\n\n")

# Run D statistic for each trait
results <- data.frame()

for (trait in traits_to_test) {
    cat("  Testing:", trait, "...")
    tryCatch({
        # Subset to non-NA
        sub <- traits_matched[!is.na(traits_matched[[trait]]), ]
        sub_comp <- comparative.data(
            phy  = tree_ultra,
            data = sub,
            names.col = "accession",
            warn.dropped = FALSE
        )

        d_result <- phylo.d(
            data     = sub_comp,
            binvar   = as.name(trait),
            permut   = 1000
        )

        results <- rbind(results, data.frame(
            trait        = trait,
            D            = d_result$DEstimate,
            p_random     = d_result$Pval1,   # p vs random (D=1)
            p_brownian   = d_result$Pval0,   # p vs Brownian (D=0)
            n_ones       = sum(sub[[trait]] == 1, na.rm=TRUE),
            n_zeros      = sum(sub[[trait]] == 0, na.rm=TRUE)
        ))
        cat(" D =", round(d_result$DEstimate, 3), "\n")

    }, error=function(e) {
        cat(" ERROR:", conditionMessage(e), "\n")
    })
}

cat("\n=== RESULTS ===\n")
results$interpretation <- ifelse(
    results$D < 0, "Stronger than Brownian (clumped)",
    ifelse(results$D < 1, "Between Brownian and random",
    ifelse(results$D == 1, "Random", "Overdispersed"))
)
results$significant_vs_random    <- results$p_random < 0.05
results$significant_vs_brownian  <- results$p_brownian < 0.05

print(results[order(results$D), ])

write.csv(results, "11_phylo_stats/d_statistic_results.csv",
          row.names=FALSE)
cat("\n✓ Saved: 11_phylo_stats/d_statistic_results.csv\n")

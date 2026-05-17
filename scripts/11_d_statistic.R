library(caper)
library(ape)
library(phytools)

cat("=== D Statistic Analysis — Yersinia AMR traits ===\n\n")

# ── Load + prepare tree ───────────────────────────────────────────────────────
cat("Loading tree...\n")
tree <- read.tree("10_gwas/rpoB_tree_scoary2.nwk")
cat("Tips:", length(tree$tip.label), "\n")

# Root + resolve polytomies
if (!is.rooted(tree)) tree <- midpoint.root(tree)
tree <- multi2di(tree)

# Force ultrametric
tree_ultra <- force.ultrametric(tree, method="extend")

# Fix zero-length branches (add tiny epsilon)
min_bl <- min(tree_ultra$edge.length[tree_ultra$edge.length > 0])
zero_idx <- tree_ultra$edge.length <= 0
n_zero <- sum(zero_idx)
if (n_zero > 0) {
    tree_ultra$edge.length[zero_idx] <- min_bl * 0.001
    cat("Fixed", n_zero, "zero-length branches\n")
}
cat("Ultrametric:", is.ultrametric(tree_ultra), "\n")
cat("Min branch length:", min(tree_ultra$edge.length), "\n\n")

# ── Load traits ───────────────────────────────────────────────────────────────
cat("Loading traits...\n")
traits <- read.csv("11_phylo_stats/d_statistic_traits.csv",
                   stringsAsFactors=FALSE)
traits <- traits[traits$accession %in% tree_ultra$tip.label, ]
rownames(traits) <- traits$accession
cat("Matched:", nrow(traits), "genomes\n\n")

# ── Traits to test ────────────────────────────────────────────────────────────
traits_to_test <- c(
    "niche_H", "niche_A", "niche_F", "niche_E",
    "amr_blaA", "amr_vat_F_", "amr_blaYRC",
    "amr_tet_A_", "amr_sul2", "amr_sul1",
    "amr_aadA1", "amr_aadA12", "amr_floR",
    "amr_sat2", "amr_dfrA1", "amr_qacEdelta1",
    "has_plasmid"
)
traits_to_test <- traits_to_test[traits_to_test %in% colnames(traits)]
cat("Testing", length(traits_to_test), "traits\n\n")

# ── Run D statistic ───────────────────────────────────────────────────────────
results <- list()

for (trait in traits_to_test) {
    cat("  Testing:", trait, "...")
    tryCatch({
        tmp <- data.frame(
            accession = rownames(traits),
            TRAIT     = as.integer(traits[[trait]]),
            stringsAsFactors = FALSE
        )
        # Check trait has both 0 and 1
        n1 <- sum(tmp$TRAIT == 1, na.rm=TRUE)
        n0 <- sum(tmp$TRAIT == 0, na.rm=TRUE)
        if (n1 < 2 || n0 < 2) {
            cat(" SKIP (n1=", n1, "n0=", n0, ")\n")
            next
        }
        tmp_cd <- comparative.data(
            phy          = tree_ultra,
            data         = tmp,
            names.col    = "accession",
            warn.dropped = FALSE
        )
        d_result <- phylo.d(
            data   = tmp_cd,
            binvar = TRAIT,
            permut = 1000
        )
        results[[trait]] <- data.frame(
            trait        = trait,
            D            = round(d_result$DEstimate, 4),
            p_random     = round(d_result$Pval1, 4),
            p_brownian   = round(d_result$Pval0, 4),
            n_present    = n1,
            n_absent     = n0,
            interpretation = ifelse(
                d_result$DEstimate <= 0,  "Clumped > Brownian",
                ifelse(d_result$DEstimate < 1,  "Phylogenetic signal",
                ifelse(abs(d_result$DEstimate - 1) < 0.05, "Random",
                                                            "Overdispersed"))),
            stringsAsFactors = FALSE
        )
        cat(" D =", round(d_result$DEstimate,4),
            "| p_rand =", round(d_result$Pval1,4),
            "| p_BM =",   round(d_result$Pval0,4), "\n")
    }, error = function(e) {
        cat(" ERROR:", conditionMessage(e), "\n")
    })
}

# ── Save ──────────────────────────────────────────────────────────────────────
df_results <- do.call(rbind, results)

if (!is.null(df_results) && nrow(df_results) > 0) {
    write.csv(df_results, "11_phylo_stats/d_statistic_results.csv",
              row.names=FALSE)
    cat("\n=== RESULTS (sorted by D) ===\n")
    print(df_results[order(df_results$D), ], row.names=FALSE)
} else {
    cat("\nNo results computed\n")
}
cat("\n✓ Done:", format(Sys.time()), "\n")

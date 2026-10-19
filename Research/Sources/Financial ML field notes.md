# Financial ML Validation: Field Notes and Reading Leads

> This is a **methodology lead note**, not a substitute for the cited papers. The working source grade below reflects the known usefulness of the recommended literature, not a claim of fresh exhaustive review.

- **Evidence grade:** 4 for the curated methodological reading leads; individual references have separate grades below. This note itself is a secondary reading map.
- **Recency:** References date mainly from 2014–2018; verify later methods and applicability.
- **Novelty:** Low-to-medium; established practitioner methodology synthesized as a navigation lead.
- **Source type:** Secondary bibliography and practitioner-oriented research note.

## Core idea

Financial observations are time-dependent, overlapping, and nonstationary. Random cross-validation can leak information across adjacent or overlapping labels. Chronological evaluation, purging of overlapping label intervals, embargo gaps, nested selection, and complete trial logging are common controls discussed in the financial ML literature.

## First reading leads

- Marcos López de Prado, *Advances in Financial Machine Learning* (2018): book source; **Grade 4** for a specialized practitioner-oriented synthesis. Copyrighted; obtain through a lawful source. Review methods critically and compare with primary papers.
- David H. Bailey et al., “The Probability of Backtest Overfitting” (2014): **Grade 3** methodological working-paper/journal literature lead; study the assumptions and later discussion before selecting a correction.
- Bailey & López de Prado, “The Deflated Sharpe Ratio: Correcting for Selection Bias, Backtest Overfitting and Non-Normality” (2014): **Grade 3** technical-method paper lead; examine the full derivation, applicability, and assumptions.
- [[Harvey Liu Zhu 2016]] and [[Novy-Marx 2015]]: academic multiple-testing/selection foundations.

## Practical checklist

- Define each sample by what was known at the time.
- Use chronology for train/validation/test, and account for overlapping targets.
- Choose features, thresholds, and hyperparameters only inside training/validation folds.
- Keep an experiment ledger of all attempts; a holdout loses its protection if repeatedly inspected.
- Report forecast, risk, execution, and net-performance metrics separately.
- Test multiple-testing and selection effects; no one metric “fixes” a contaminated research process.

## Connected notes

[[ML validation]] · [[Overfitting controls]] · [[Edge validation]] · [[Research workflow]]

## Copyright note

The book is copyrighted; no copy is included. Paper copies should only be added when distribution rights permit.

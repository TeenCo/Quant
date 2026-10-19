# Inventory the LSE Catalog

This helper snapshots the **metadata catalog only**. It does not request history, live ticks, options prints, or reference datasets.

## Prerequisites

1. Obtain an API key from the official London Strategic Edge account/data portal.
2. Install a current supported Python release and the provider SDK in a dedicated environment:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install lse-data
```

3. Run the script from PowerShell; it prompts for the API key with hidden input and does not save the key:

```powershell
python "Research\Tools\inventory_lse_catalog.py" "C:\Users\Dell\Desktop\Quant\private-lse-catalog"
```

Then collect current vault structure, reference-table inventory, and usage/quota metadata (still no history rows) with:

```powershell
python "Research\Tools\lse_metadata_preflight.py" "C:\Users\Dell\Desktop\Quant\private-lse-catalog\preflight"
```

After reviewing those results, generate—without making API requests—a representative bounded sample plan from the local catalog snapshot:

```powershell
python "Research\Tools\build_lse_sample_plan.py" "C:\Users\Dell\Desktop\Quant\private-lse-catalog\lse_catalog_YYYYMMDDTHHMMSSZ.json"
```

This chooses up to three candidate symbols per dataset (largest/median catalog tick metadata and oldest history start), proposes short date windows and method hints, and marks all items `planned_only_not_requested`. It is a review queue, not an instruction to execute every call; resolve dataset terms, schema, method compatibility, and export quotas first.

Replace the output path with a private local directory that is not synchronized or shared unless provider terms allow it. The script writes timestamped JSON and CSV catalog metadata and prints the number of returned catalog rows. It records the package version and retrieval time. It does not claim that catalog rows imply complete or point-in-time history.

## After the snapshot

Compare categories, symbols, date spans, timeframes, and row-level metadata with [[Exhaustive dataset inventory and transformation protocol]]. Reconcile duplicates and unsupported symbols; then inspect `GET /vault/usage` and current terms before selecting any historical exports. Do **not** immediately export every instrument/timeframe: first estimate job/storage requirements and classify data rights and point-in-time limitations.

The preflight records only metadata endpoints: the vault's supported classes/timeframes, all catalog rows, reference-dataset counts/spans when supplied, and usage information. Review any endpoint error locally; the script suppresses exception details and records only error types.

For a bounded, row-limited schema test across supported product families, see [[Tools/Sample LSE endpoint schemas]]. It is an opt-in follow-up and still requires local key entry.

The key is entered only in the local prompt and is not written to the snapshot. The LSE SDK is MIT-licensed; retrieved data have separate terms. Do not redistribute raw data/catalog output or make it available to third parties unless current terms explicitly permit.

## Helper

[Open the Python script](inventory_lse_catalog.py)

# VNOJ Importer Research Workflow

1. Read the supplied importer source.
2. Enumerate every `self.package.read(...)`, `self.package.open(...)`, XML lookup, JSON key access and file path construction.
3. Convert these operations into explicit package assertions.
4. Compare those assertions against the supplied golden package.
5. Create an offline verifier implementation for the actual host OS.
6. Run the verifier on the golden package to establish the expected baseline.
7. Run it on the newly generated package.
8. Fix source/generator/package logic when a check fails; never patch generated input/output manually.
9. Rebuild the package and run the entire verification chain again.

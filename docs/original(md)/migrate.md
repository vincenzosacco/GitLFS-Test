# Comando `git lfs migrate`

`git lfs migrate` è un comando che consente di migrare file già presenti nel repository da Git a Git LFS e viceversa. [*Documentazione ufficiale*](https://github.com/git-lfs/git-lfs/blob/main/docs/man/git-lfs-migrate.adoc)

- ### `import`
  migra i file già presenti nel repository a Git LFS. Nello specifico trasforma gli oggetti Git in [puntatori Git LFS](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-git-large-file-storage?versionId=free-pro-team%40latest&productId=repositories&restPage=managing-your-repositorys-settings-and-features%2Cmanaging-repository-settings%2Cmanaging-git-lfs-objects-in-archives-of-your-repository#pointer-file-format)


    ***Nota*** - è sempre possibile fare il 'revert' di questa operazione, ovvero migrare i file da Git LFS a Git, usando il comando `git lfs migrate export` (vedi sotto).

- ### `export`
  esattamente l'opposto di `git lfs migrate import`.
  ```shell
  # Migra tutti i file '.ext' da Git LFS a Git
  git lfs migrate export --include="*.ext"

  # Migra tutti i file più grandi di 100MB da Git LFS a Git
  git lfs migrate export --above=100MB
  ```

## Opzioni più comuni
- `--include`: specifica i file da includere nella migrazione.
- `--exclude`: specifica i file da escludere dalla migrazione.
- `--above`: specifica una dimensione minima per i file da migrare. Ad esempio, `--above=100MB` migrerà solo i file più grandi di 100 MB.
- `--everything`: opera su tutti i riferimenti del file in ogni branch e tag.
- `--no-rewrite`: non riscrive la cronologia dei commit, utile se vuoi mantenere i commit originali.



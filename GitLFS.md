# Come Caricare File di Grandi Dimensioni su GitHub Usando Git LFS

## Passo 1: Installare Git LFS

Prima di tutto, assicurati che Git LFS sia installato sul tuo sistema. Puoi installarlo da [git-lfs.github.com](https://git-lfs.github.com/) o utilizzare un package manager.

- Per Windows (usando Chocolatey): `choco install git-lfs`
- Per macOS: `brew install git-lfs`
- Per Linux: `sudo apt install git-lfs` (Ubuntu/Debian) o simili per la tua distribuzione.

Dopo l'installazione, inizializza Git LFS:
``` shell
git lfs install
```

## Passo 2: Traccia il File di Grandi Dimensioni
1. Vai nella cartella del tuo repository tramite terminale.
2. Per tracciare un file di grandi dimensioni, i comandi variano a seconda che il file sia già presente nel repository o meno:
    
    - Se il file *non è ancora presente in un commit*, puoi usare:
      ``` shell
      git lfs track "nomefile.ext"
      ```
      è anche possibile tracciare tutti i file con una certa estensione:
      ``` shell
      git lfs track "*.ext"
      ```

     - Se il file *è già presente in un commit*, bisogna [migrare](#git-lfs-migrate-import-quali-opzioni-usare) i large files già tracciati da Git su Git LFS. 

3. I comandi precedenti creano un file *.gitattributes* nel tuo repository che indica a Git di usare LFS per il file specificato. Aggiungi questo file al working tree se non è già presente:
    ``` shell
    git add .gitattributes
    ```

*Per verificare quali file sono tracciati da LFS, puoi usare il comando:*
``` shell
git lfs ls-files
```

## Passo 3: Aggiungi il File di Grandi Dimensioni
- Aggiungi il file al tuo repository con il comando:
    ``` shell
    git add nomefile.ext
    ```

## Passo 4: Effettua il Commit delle Modifiche
-  Esegui il commit delle modifiche con un messaggio descrittivo:
    ``` shell
      git commit -m "Aggiunta nomefile.ext (large file)"
    ```

## Passo 5: Esegui il Push su GitHub
- Infine, esegui il push delle modifiche sul repository GitHub:
  ```
  git push origin main
  ```
- Sostituisci `main` con il nome del tuo branch se ne stai usando uno diverso.

## Passo 6: Verifica il Caricamento
- Vai sul tuo repository GitHub tramite browser e verifica che il file sia stato caricato correttamente.


## Note Aggiuntive
- Tieni presente i [limiti di spazio e banda associati](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-storage-and-bandwidth-usage) a Git LFS su GitHub, e [monitora l'utilizzo del tuo spazio]([htt](https://docs.github.com/en/billing/managing-billing-for-your-products/managing-billing-for-git-large-file-storage/viewing-your-git-large-file-storage-usage)).

# `git lfs migrate import` quali opzioni usare?
Quando si migra un file già presente nel repository, è possibile usare il comando `git lfs migrate import` per spostare i file già tracciati da Git su Git LFS. Questa operazione si può fare in due modi:
- **Riscrivendo la cronologia dei commit**: questo metodo riscrive la cronologia del repository, il che significa che sarà necessario forzare il push (`git push --force`) e i collaboratori dovranno risincronizzare i loro repository locali.
##




- `--include`: specifica i file da includere nella migrazione.
- `--exclude`: specifica i file da escludere dalla migrazione.
- `--everything`: migra tutti i file nel repository, non solo quelli tracciati da LFS.
- `--no-rewrite`: non riscrive la cronologia dei commit, utile se vuoi mantenere i commit originali.

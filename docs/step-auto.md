# Come Caricare File di Grandi Dimensioni su GitHub Usando Git LFS - versione 'Automatica'


### Passo 1: Traccia il File di Grandi Dimensioni
1. Vai nella cartella del tuo repository tramite terminale.
2. Per tracciare un file di grandi dimensioni, i comandi variano a seconda che il file sia già presente nel repository o meno:
    
    - Se il file [*non è ancora presente in un commit*](https://github.com/git-lfs/git-lfs/blob/main/docs/man/git-lfs-migrate.adoc#migrate-unpushed-commits), puoi usare:
      ``` shell
      # Un file specifico
      git lfs migrate import --include="nomefile.ext"
      # Tutti i file con estensione .ext
      git lfs migrate import --include="*.ext"
      # Tutti i file con estensione più grandi di 100MB
      git lfs migrate import --above=100MB
      # Tutti i file con estensione .ext più grandi di 100MB
      git lfs migrate import --above=100MB --include="*.ext"
      ```

     - Se il file *è già presente in un commit*, bisogna [migrare](#git-lfs-migrate-import-quali-opzioni-usare) i large files già tracciati da Git su Git LFS. 


I comandi precedenti creano o aggiornano il file *.gitattributes* e lo aggiungono al commit.

*Per verificare quali file sono tracciati da LFS, puoi usare il comando:*
``` shell
git lfs ls-files
```

### Passo 2: Aggiungi il File di Grandi Dimensioni
- Aggiungi il file al tuo repository con il comando:
    ``` shell
    git add nomefile.ext
    ```

### Passo 3: Effettua il Commit delle Modifiche
-  Esegui il commit delle modifiche con un messaggio descrittivo:
    ``` shell
      git commit -m "Aggiunta nomefile.ext (large file)"
    ```

### Passo 4: Esegui il Push su GitHub
- Infine, esegui il push delle modifiche sul repository GitHub:
  ```shell
  # Se non hai modificato la history al passo 1
  git push
  # Se hai modificato la history al passo 1
  git push --force
  ```


<!--   -->
# `git lfs migrate import` quali opzioni usare?
Quando si migra un file già presente nel repository, è possibile usare il comando [`git lfs migrate import`](https://github.com/git-lfs/git-lfs/blob/main/docs/man/git-lfs-migrate.adoc#git-lfs-migrate1) per spostare i file già tracciati da Git su Git LFS. Questa operazione si può fare in due modi:
- **[Riscrivendo la cronologia dei commit](https://github.com/git-lfs/git-lfs/blob/main/docs/man/git-lfs-migrate.adoc#migrate-local-history)**: questo metodo riscrive la cronologia del repository, il che significa che sarà necessario forzare il push (`git push --force`)
  ```shell 
  # Attivo in tutti i branch
  git lfs migrate import --everything --include="*.ext"
  ```
  
  *Vantaggi*: riduce la dimensione del repository e migliora le prestazioni.
  *Svantaggi*: modifica la cronologia, il che può essere problematico per i collaboratori.

- **[Non riscrivendo la cronologia dei commit](https://github.com/git-lfs/git-lfs/blob/main/docs/man/git-lfs-migrate.adoc#migrate-without-rewriting-local-history)**: questo metodo non modifica la cronologia del repository, ma crea un nuovo commit con i file migrati su LFS.
  
  ``` shell 
  # Senza messaggio di commit
  git lfs migrate import --everything --include="*.ext" --no-rewrite
  
  # Con messaggio di commit
  git lfs migrate import --everything --include="*.ext" --no-rewrite -m "Migrato file di grandi dimensioni su LFS"
  ```

  *Vantaggi*: non modifica la cronologia, quindi è più comodo per i collaboratori.
  
  *Svantaggi*: le ottimizzazioni delle dimensioni saranno efficaci solo per i nuovi commit, non per quelli già esistenti.

  
## Opzioni più comuni
- `--include`: specifica i file da includere nella migrazione.
- `--exclude`: specifica i file da escludere dalla migrazione.
- `--above`: specifica una dimensione minima per i file da migrare. Ad esempio, `--above=100MB` migrerà solo i file più grandi di 100 MB.
- `--everything`: migra tutti i file nel repository, non solo quelli tracciati da LFS.
- `--no-rewrite`: non riscrive la cronologia dei commit, utile se vuoi mantenere i commit originali.



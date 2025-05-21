# Migrare file di grandi dimensioni (già presenti nella repo) su Git LFS - migrate 'rewrite'

Questo metodo è utilizzato per 'migrare' la gestione dell'archiviazione di file già presenti nei commit da Git a Git LFS **riscrivendo la cronologia dei commit**.

## *Vantaggi*
  - Permette di **caricare su GitHub una repo che contiene già file più grandi di 100MB** (limite imposto).
  - Ottimizzazione dello spazio: i file di grandi dimensioni vengono spostati in Git LFS, riducendo la dimensione del repository.
  
## *Svantaggi*
  - Bisogna forzare il push (`git push --force`), quindi potrebbe causare problemi a chi ha già clonato il repository. 

### 1. Traccia e Migra il File di Grandi Dimensioni
1. Vai nella cartella del tuo repository tramite terminale.
2. Per tracciare un file di grandi dimensioni 
    ```shell
    # Un file specifico
    git lfs migrate import --include="nomefile.ext" --everything
    
    # Tutti i file con estensione '.ext'
    git lfs migrate import --include="*.ext"  --everything

    # Tutti i file con estensione più grandi di 100MB
    git lfs migrate import --above=100MB --everything
    
    # Tutti i file '.ext' più grandi di 100MB
    git lfs migrate import --above=100MB --include="*.ext" --everything
    ```

  *`--everything` indica di migrare i file in tutti i branch. [Info](steps-migrate.md#opzioni-più-comuni)*

  I comandi precedenti creano o aggiornano il file *.gitattributes* e lo aggiungono al commit.
  *Per verificare quali file sono tracciati da LFS, puoi usare:* 
  ```shell
  git lfs ls-files
  ```


### 2.  Esegui il Push su GitHub
Il comando `git lfs migrate import` ha già creato un commit con i file migrati su LFS, quindi ora basta eseguire il push delle modifiche sul repository GitHub:
  ```shell
  git push --force
  ```



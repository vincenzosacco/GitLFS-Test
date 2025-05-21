# Migrare file di grandi dimensioni (già presenti nella repo) su Git LFS - migrate 'no-rewrite'

Questo metodo è utilizzato per 'migrare' la gestione dell'archiviazione di file già presenti nei commit da Git a Git LFS **senza riscrivere la cronologia dei commit**. 

## ***Vantaggi***
- Non riscrive la cronologia dei commit, quindi non è necessario forzare il push.

## ***Svantaggi***
- **Genera errori** se il file non è presente nei commit della remote ( dovuto a `--no-rewrite`).
- Non rimuove i file di grandi dimensioni dalla cronologia dei commit, quindi il repository rimarrà grande.
 

### 1. Traccia il File di Grandi Dimensioni
1. Vai nella cartella del tuo repository tramite terminale.
2. Per tracciare un file di grandi dimensioni 
    ```bash
    # Un file specifico
    git lfs migrate import --include="nomefile.ext" --no-rewrite
    
    # Tutti i file con estensione .ext
    git lfs migrate import --include="*.ext" --no-rewrite
    # Tutti i file con estensione più grandi di 100MB
    git lfs migrate import --above=100MB --no-rewrite
    # Tutti i file con estensione .ext più grandi di 100MB
    git lfs migrate import --above=100MB --include="*.ext" --no-rewrite
    ```


  I comandi precedenti creano o aggiornano il file *.gitattributes* e lo aggiungono al commit.
  *Per verificare quali file sono tracciati da LFS, puoi usare:*
  ``` bash
  git lfs ls-files
  ```

### 2.  Esegui il Push su GitHub
Il comando `git lfs migrate import` ha già creato un commit con i file migrati su LFS, quindi ora basta eseguire il push delle modifiche sul repository GitHub:
  ``` bash
  git push
  ```

## Troubleshooting

### ERROR: Expected one or more files with --no-rewrite
Si verifica quando si esegue il comando `git lfs migrate import` con l'opzione `--no-rewrite` e GitLFS non trova nei **commit della remote** i file specificati da `--include`,`--exclude` o `--above`. 
Assicurati che:
- I file esistono nei commit della remote.
- Il nome dei file specificati sono corretti. 

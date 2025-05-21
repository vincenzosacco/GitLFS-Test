# Come Caricare File di Grandi Dimensioni su GitHub Usando Git LFS - versione 'Track'
Questo metodo è utilizzato per 'tracciare' file di grandi dimensioni **senza riscrivere la cronologia dei commit**.

## *Vantaggi*
  - non è necessario forzare il push (`git push --force`), quindi non causa 'fastidi' a chi ha già clonato il repository. E' bene sottolinereare in questo caso forzare il push non causerebbe problemi di integrità, come spiegato [qui](migrate.md#import).
  
## *Svantaggi*
  - **non è utile se si vuole caricare una repo su GitHub che contiene già file più grandi di 100MB** (limite imposto). Per fare questo, seguire il [metodo 'migrate rewrite'](steps-rewrite.md).

  - l'ottimizzazione dello spazio non è così efficace come nel [metodo 'migrate rewrite'](steps-rewrite.md), in quanto [tracciamento LFS](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-git-large-file-storage#about-git-large-file-storage) viene abilitato solo nei commit successivi al [passo 3](#passo-3-effettua-il-commit-delle-modifiche).

### 1. Traccia il File di Grandi Dimensioni
  1. Vai nella cartella del tuo repository tramite terminale.
  2. Per tracciare un file di grandi dimensioni:
        ``` shell
        # Tracciare un file specifico:
        git lfs track "nomefile.ext"

        # Tracciare tutti i file con una certa estensione:
        git lfs track "*.ext"
        ```

  3. A questo punto è stato creato/aggiornato il file [*.gitattributes*](https://github.com/gitattributes/gitattributes) nel tuo repository. Aggiungi questo file al working tree se non è già presente:
      ``` shell
      git add .gitattributes
      ```

*Per verificare quali file sono tracciati da LFS, puoi usare il comando:*
``` shell
git lfs ls-files
```

### 2. Aggiungi il File di Grandi Dimensioni
  - Se il file *non è ancora presente in un commit* :
      ``` shell
      git add nomefile.ext
      ``` 


### 3. Effettua il Commit delle Modifiche
-  Esegui il commit delle modifiche:
    ``` shell
    git commit -m "Aggiunta nomefile.ext (large file) con tracciamento LFS"  
    ```

### 4.  Esegui il Push su GitHub
- Infine, esegui il push delle modifiche sul repository GitHub:
  ```shell
  git push
  ```

Da questo momento, Git LFS gestirà i file specificati nel file *.gitattributes*.



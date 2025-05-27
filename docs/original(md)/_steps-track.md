# Come Caricare File di Grandi Dimensioni su GitHub Usando Git LFS - versione 'Track'
Questo metodo è utilizzato per 'tracciare' file di grandi dimensioni **senza riscrivere la cronologia dei commit**.

## *Vantaggi*
  - non è necessario forzare il push (`git push --force`), quindi non causa 'fastidi' a chi ha già clonato il repository. E' bene sottolineare che in questo caso forzare il push non causerebbe problemi di integrità, come spiegato [qui](_migrate.md#import).
  
## *Svantaggi*
  - **non è utile se si vuole caricare una repo su GitHub che contiene già file più grandi di 100MB** (limite imposto). Per fare questo, seguire il [metodo 'migrate rewrite'](_steps-rewrite.md).

  - l'ottimizzazione dello spazio non è così efficace come nel [metodo 'migrate rewrite'](_steps-rewrite.md), in quanto [tracciamento LFS](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-git-large-file-storage#about-git-large-file-storage) viene abilitato solo nei commit successivi al [passo 3](#passo-3-effettua-il-commit-delle-modifiche).

### 1. Traccia il File di Grandi Dimensioni
  1. Vai nella cartella del tuo repository tramite terminale.
  2. Per tracciare un file di grandi dimensioni:
        ```bash
        # Tracciare un file specifico:
        git lfs track "nomefile.ext"

        # Tracciare tutti i file con una certa estensione:
        git lfs track "*.ext"
        ```

  3. A questo punto è stato creato/aggiornato il file [*.gitattributes*](https://github.com/gitattributes/gitattributes) nel tuo repository. Aggiungi questo file al working tree se non è già presente:
      ```bash
      git add .gitattributes
      ```

*Per verificare quali file sono tracciati da LFS, puoi usare il comando:*
  ```bash
  git lfs ls-files
  ```





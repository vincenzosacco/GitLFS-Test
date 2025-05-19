# Come Caricare File di Grandi Dimensioni su GitHub Usando Git LFS

### Installare Git LFS

Prima di tutto, assicurati che Git LFS sia installato sul tuo sistema. Puoi installarlo da [git-lfs.github.com](https://git-lfs.github.com/) o utilizzare un package manager.

- Per Windows (usando Chocolatey): `choco install git-lfs`
- Per macOS: `brew install git-lfs`
- Per Linux: `sudo apt install git-lfs` (Ubuntu/Debian) o simili per la tua distribuzione.

Dopo l'installazione, inizializza Git LFS:
``` shell
# Inizializza Git LFS a livello globale
git lfs install
```
``` shell
# Inizializza Git LFS solo per il repository corrente
git lfs install --local
```

### Tracciare File di Grandi Dimensioni
A questo punto, puoi scegliere tra due metodi: [Automatica](step-auto.md) o [Manuale](step-manual.md).



## Note Aggiuntive
- Tieni presente i [limiti di spazio e banda associati](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-storage-and-bandwidth-usage) a Git LFS su GitHub, e [monitora l'utilizzo del tuo spazio](https://docs.github.com/en/billing/managing-billing-for-your-products/managing-billing-for-git-large-file-storage/viewing-your-git-large-file-storage-usage).
- Anche chi clona la repo deve eseguire il [passo 1](#passo-1-installare-git-lfs)
- Per clonare la repo utilizzare ```git lfs clone```
- Se la repo è già clonata da prima che fosse abilitato LFS, utilizzare il comando:
``` shell
git lfs pull
```

  
<!-- TROUBLESHOOTING -->
# Troubleshooting
### Ho clonato la repo ma non riesco a vedere i file di grandi dimensioni.
- Assicurati di avere installato Git LFS e di aver eseguito `git lfs install`.
- Prova a eseguire `git lfs pull` per scaricare i file di grandi dimensioni.
  



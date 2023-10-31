def decrypt(ciphertext, key):
    plaintext = ''
    n = 0
    for p in range(0, len(ciphertext)):
        if n > len(ciphertext):
            break
        else:
            try:
                plaintext = plaintext + ciphertext[n]
            except IndexError:
                break
        n = n + (key+1)
    return plaintext

print(decrypt('YFwoJeELOvlDVrOlNBDConouLwhdCC mkIjsYeKsuaGsDbSRJymLJVOaYNQRrgKBSifPOdnCbUleWCbf', 4))
print(decrypt('HNABntvVepMaQSNHyKxQTXZf HVbQXcqJSXfswOAuRBzpefOdfBeylimeqDHDlFc', 7))
print(decrypt('PqKgakYBpfzveAHVrrUgbzpkaMWUcskukxac QfsWpFSrTrwiaQRtSsXesGlrBqv', 3))
print(decrypt('HXelrEed fCxojmVersu Gtehvee NSluGnJ', 1))
print(decrypt('PHcRrveeRUmDnfqMFAnBJvvwyzSDrj tqXhrLRXIegaDLwdInIGCvqelcjzU', 5))
print(decrypt(''))
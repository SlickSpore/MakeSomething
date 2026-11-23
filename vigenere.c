#define vigenere(a, b, m) for (char *c = (a); *c != '\0'; ) for (const char *k = (b); *c != '\0' && *k != '\0'; k++, c++) *c = (m) ? (*c + *k) % 128 : (*c - *k + 128) % 128

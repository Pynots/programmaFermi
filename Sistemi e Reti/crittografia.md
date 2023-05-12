# La Crittografia

**criptare** un messaggio significa renderlo illegibile agli occhi altrui

**decriptare** un messaggio significa renderlo leggibile agli occhi altrui


Esistono 4 tipi diversi di crittografia:



## Simmetrica

La crittografia simmetrica si basa su un'unica **chiave** posseduta da entrambi gli utenti.
Essi la usano per criptare e decriptare i messaggi che si inviano tra di loro.

## Asimmetrica

La crittografia asimmetrica si basa sul fatto che ogni utente ha 2 chiavi: una **pubblica** e una **privata**:

**Pubblica**: è la chiave utilizzata dall'utente e che anche gli altri utenti possono vedere e conoscere.

**Privata**: è la chiave che solo il proprietario conosce.

Il primo utente cripta il messaggio con la chiave pubblica del secondo utente. Il secondo utente, invece, decripta il messaggio mediante la sua chiave privata, poichè solo lui può vederla.

Se però un utente malintenzionato intercetta il messaggio, lo elimina, lo riscrive e lo cripta con la sua chiave pubblica; io che lo ricevo non posso capire da chi mi arriva.

## doppia
 
La crittografia doppia si basa sul funzionamento della crittografia asimmetrica, ma gli aggiunge una cifratura in più, rendendo così necessario che il primo utente utilizzi anche la sua chiave pubblica per decifrare il messaggio criptato dal secondo utente.

Così facendo però risulta molto più faticoso e costoso.

## di sessione

La crittografia di sessione usa la crittografia asimmetrica per scambiarsi una chiave da utilizzare per la crittografia simmetrica.

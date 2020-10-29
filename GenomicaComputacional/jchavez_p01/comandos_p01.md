#Comandos de la Práctica 01
##Jorge Adrian Chávez Cid

#Parte I

Comandos:
```mkdir -p GenomicaComputacional/jchavez_p01```
```nano comandos_p01.md```

**Respuesta 1**
```echo $0```
bash
echo $SHELL
/bin/bash

**Respuesta 2**
```mkdir data filtered raw_data meta scripts figures archive```
Verificamos con ```ls```

**Respuesta 3**
```mv filtered/ /home/adriancid/Documents/Computational-Genomics-Notes/GenomicaComputacional/jchavez_p01/data/```
```mv raw_data/ /home/adriancid/Documents/Computational-Genomics-Notes/GenomicaComputacional/jchavez_p01/data/```

**Respuesta 4**


#Parte II

**Respuesta 1**
Antes: -rw-rw-r-- delay.sh
```chmod +x delay.sh```

**Respuesta 2**
Después: -rwxrwxr-x delay.sh
```sh delay.sh```

**Respuesta 3**
```sleep 30```

**Respuesta 4**
```sh delay.sh &```
[1] 2472
```kill -9 2472```
[1]+ Killed  sh delay.sh


#Parte 3

**Respuesta 2**
```mv sequence.fasta sarscov2_genome.fasta```
```mv sequence.gff3 sarscov2_genome.gff3```
```mv sequence.fasta splike_c.faa```
```mv 'sequence(1).fasta' splike_b.faa```
```mv 'sequence(2).fasta' splike_a.faa```

```mv *.faa *.gz *.fasta *.gff3 /home/adriancid/Documents/Computational-Genomics-Notes/GenomicaComputacional/jchavez_p01/data/raw_data/```


#Parte 4

**Respuesta 1**
```ln -s splike_c.faa ../filtered/lns_splike_c```
```ln -s splike_b.faa ../filtered/lns_splike_b```
```ln -s splike_a.faa ../filtered/lns_splike_a```

**Respuesta 2**





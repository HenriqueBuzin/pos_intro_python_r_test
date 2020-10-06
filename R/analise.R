setwd("C:/Users/henri/Desktop/pos_intro_python_r_test/R/")
df <- read.csv(file = "paises.csv", header = TRUE, sep = ",")

total = df["Populacao"].sum()

df2 <- aggregate(df["Populacao"], df["Regiao"], FUN = sum)

slices <- c(df2$Populacao)
lbls <- c(df2$Regiao)
pie(slices, labels = lbls, main="População por Região")


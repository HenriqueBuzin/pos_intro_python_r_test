setwd("C:/Users/henri/Desktop/pos_intro_python_r_test/R/")
df <- read.csv(file = "paises.csv", header = TRUE, sep = ",")

df2 <- aggregate(df["Populacao"], df["Regiao"], FUN = sum)

slices <- c(df2$Populacao)
lbls <- c(df2$Regiao)
pct <- round(slices/sum(slices)*100)
lbls <- paste(lbls, pct)
lbls <- paste(lbls,"%",sep="")
pie(slices,labels = lbls, col=rainbow(length(lbls)),main="População por Região")


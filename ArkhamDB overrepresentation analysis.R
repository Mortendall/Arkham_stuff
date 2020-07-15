library(rvest)
library(selectr)  
library(xml2)  
library(stringr)  
library(magicfor)

#I have subsequently found that the URL can change. Generate a list of URLs using this code:
ID <- "02001"
card <- "05153"
no_pages <- (1:15)
View(z)
z <- expand.grid(ID, card,no_pages)
URLlist <- paste0("https://arkhamdb.com/decklists/find/",z$Var3,"?faction=&cards%5B0%5D=",z$Var1,"&cards%5B1%5D=",z$Var2,"&author=&name=&sort=date&packs%5B0%5D=1&packs%5B1%5D=1-2&packs%5B2%5D=2&packs%5B3%5D=4&packs%5B4%5D=5&packs%5B5%5D=8&packs%5B6%5D=9&packs%5B7%5D=10&packs%5B8%5D=11&packs%5B9%5D=12&packs%5B10%5D=13&packs%5B11%5D=14&packs%5B12%5D=15&packs%5B13%5D=16&packs%5B14%5D=17&packs%5B15%5D=18&packs%5B16%5D=20&packs%5B17%5D=21&packs%5B18%5D=22&packs%5B19%5D=23&packs%5B20%5D=24&packs%5B21%5D=25&packs%5B22%5D=26&packs%5B23%5D=29&packs%5B24%5D=30&packs%5B25%5D=31&packs%5B26%5D=34&packs%5B27%5D=35&packs%5B28%5D=36&packs%5B29%5D=37&packs%5B30%5D=38&packs%5B31%5D=40&packs%5B32%5D=41&packs%5B33%5D=42&packs%5B34%5D=43&packs%5B35%5D=44&packs%5B36%5D=45&packs%5B37%5D=52&packs%5B38%5D=28&packs%5B39%5D=33&packs%5B40%5D=39&packs%5B41%5D=3&packs%5B42%5D=6&packs%5B43%5D=27&packs%5B44%5D=32&packs%5B45%5D=46&packs%5B46%5D=19&packs%5B47%5D=7&packs%5B48%5D=53")
View(URLlist)

#scrape deck titles, which qualifies as unique entries w. card

magic_for(silent = T)
for(i in 1:15){
  page <- read_html(URLlist[i])
  deck_html<- html_nodes(page, ".decklist-name")
  deck <- html_text(deck_html)
  put(deck)
  Sys.sleep(1)
  print(i)
}
?map
Observed_result <- magic_result_as_vector()
length(Observed_result)
View(Observed_result)

#create background list
Background_list <- paste0("https://arkhamdb.com/decklists/find/",z$Var3,"?faction=&cards%5B0%5D=",z$Var1,"&author=&name=&sort=date&packs%5B0%5D=1&packs%5B1%5D=1-2&packs%5B2%5D=2&packs%5B3%5D=4&packs%5B4%5D=5&packs%5B5%5D=8&packs%5B6%5D=9&packs%5B7%5D=10&packs%5B8%5D=11&packs%5B9%5D=12&packs%5B10%5D=13&packs%5B11%5D=14&packs%5B12%5D=15&packs%5B13%5D=16&packs%5B14%5D=17&packs%5B15%5D=18&packs%5B16%5D=20&packs%5B17%5D=21&packs%5B18%5D=22&packs%5B19%5D=23&packs%5B20%5D=24&packs%5B21%5D=25&packs%5B22%5D=26&packs%5B23%5D=29&packs%5B24%5D=30&packs%5B25%5D=31&packs%5B26%5D=34&packs%5B27%5D=35&packs%5B28%5D=36&packs%5B29%5D=37&packs%5B30%5D=38&packs%5B31%5D=40&packs%5B32%5D=41&packs%5B33%5D=42&packs%5B34%5D=43&packs%5B35%5D=44&packs%5B36%5D=45&packs%5B37%5D=52&packs%5B38%5D=28&packs%5B39%5D=33&packs%5B40%5D=39&packs%5B41%5D=3&packs%5B42%5D=6&packs%5B43%5D=27&packs%5B44%5D=32&packs%5B45%5D=46&packs%5B46%5D=19&packs%5B47%5D=7&packs%5B48%5D=53")
View(Background_list)
#extract background list
for(i in 1:15){
  page <- read_html(Background_list[i])
  deck_html<- html_nodes(page, ".decklist-name")
  deck <- html_text(deck_html)
  put(deck)
  Sys.sleep(1)
}
Background_result <- magic_result_as_vector()
length(Background_result)

#scrape time stamp from list
magic_for(silent = T)
for(i in 1:15){
  page <- read_html(Background_list[i])
  deck_html<- html_nodes(page, "time")
  deck <- html_text(deck_html)
  put(deck)
  Sys.sleep(1)
}
Background_time <- magic_result_as_vector()
length(Background_time)
View(Background_time)

#date is only extracted as month and date but not year, which is problematic.
Background_combined <- data.frame(Background_result, Background_time)
View(Background_combined)

#Mr. "Rook" makes first appearance on Apr 24, 2019 so select everything before that time
Background_crop <- Background_combined[1:326,]
View(Background_crop)
#Unfortunately this step must be done manually

#check Arkhamdb for possible allies in deck
#this can be done on https://arkhamdb.com/search
#for Joe Diamond the number of possible allies is 14
#We assume each deck includes two different allies
#Hence the theoretical number of Joe decks with Rook is:
#currently, 16 investigators can take Mr. Rook

Results_Mr_Rook <- data.frame(matrix(ncol = 3, nrow = 16))
colnames(Results_Mr_Rook) <- c("Expected_no_of_decks","Observed_no_of_decks", "Investigator")
rownames(Results_Mr_Rook) <- c("Roland", "Daisy", "Carolyn", "Ashcan", "Finn", "Jenny", "Jim", "Joe", "Luke", "Mandy", "Marie", "Minh", "Norman", "Rex", "Ursula", "Zoey")
View(Results_Mr_Rook)

#Data set into table
Results_Mr_Rook[16,1] <- (nrow(Background_crop)/13)
Results_Mr_Rook[16,2] <- length(Observed_result)
View(Results_Mr_Rook)

write.csv(Results_Mr_Rook, "C:/Users/tvb217/Documents/R/Mr.Rook.csv")
getwd()


Results_Mr_Rook <- Results_Mr_Rook %>%
  mutate(Investigator = row.names(Results_Mr_Rook))
View(Results_Mr_Rook)

ggplot(Results_Mr_Rook, aes(x = Expected_no_of_decks, y = Observed_no_of_decks))+
  geom_point()+
  labs(x = "Expected no. of Decks", y = "Observed no. of Decks", title = "Mr. Rook in ArkhamDB decks")+
  geom_abline(intercept = 0, slope = 1, linetype = 3)+
  geom_text_repel(aes(label = Investigator),
                  box.padding = 0.35,
                  point.padding = 0.5)

library(ggrepel)
class(Results_Mr_Rook[1,2])

View(Results_Mr_Rook)

Results_Mr_Rook_Melt <- Results_Mr_Rook %>%
  melt(Results_Mr_Rook)

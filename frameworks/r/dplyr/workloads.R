library(dplyr)

project <- function(df) {
  return(dplyr::select(df, state, votes))
}

group_count <- function(df){ 
  return(df %>% dplyr::group_by(votes) %>% count())
}

sort <- function(df){
  return(arrange(df, desc(votes)))
}

flip_bool <- function(df){
  return(summarise(df, won = !won))
}

find_max <- function(df){
  return(summarise(df, max(votes)))
}

select <- function(df){
  return(filter(df, party == "DEM", won == TRUE, votes > 20000))
}

select_group_mean <- function(df){
  return(
    df %>% filter(won == TRUE) %>% group_by(party) %>% summarise(votes = mean(votes))
  )
}

longest_string_in_column <- function(df) {
  return(df %>% summarise(candidate = nchar(candidate)) %>% arrange(desc(candidate)))
}

join <- function(df){
  return(df %>% inner_join(df, by="unique_col"))
}

select_p90_cols <- function(df){
  return(dplyr::select(df, c(1, round(ncol(df) * 0.9))))
}

select_p90_rows <- function(df){
  return(slice(df, c(1, round(nrow(df) * 0.9))))
}

combine_cols <- function(df){
  df$combined = paste(df$candidate, df$party, df$won)
  return(df)
}


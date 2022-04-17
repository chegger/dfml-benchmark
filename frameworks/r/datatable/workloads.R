library(data.table)

project <- function(df) {
  return(df[, c("state", "votes")])
}

group_count <- function(df){ 
  return(df[,.N, by=c("party")])
}

sort <- function(df){
  return(df[order(-votes)])
}

flip_bool <- function(df){
  return(df[, won := lapply(.SD, function(x) !x), .SDcols = "won"])
}

find_max <- function(df){
  return(df[,max(votes)])
}

select <- function(df){
  return(df[party == "DEM" & won & votes > 20000])
}

select_group_mean <- function(df){
  return(df[won==TRUE, mean(votes), by = "party"])
}

longest_string_in_column <- function(df){
  return(df[, max(nchar(candidate))])
}

join <- function(df){
  return(df[df, on="unique_col", nomatch=0])
}

select_p90_cols <- function(df){
  return(df[,1:round(ncol(df) * 0.9)])
}

select_p90_rows <- function(df){
  return(df[1:round(nrow(df) * 0.9)])
}

combine_cols <- function(df){
  return(df[ , combined := do.call(paste, c(.SD, sep = " ")), .SDcols = c("candidate", "party", "won")])
}

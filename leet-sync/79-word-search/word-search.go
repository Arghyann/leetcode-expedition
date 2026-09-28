func exist(board [][]byte, word string) bool {
    flag:=false
    var visited [][2]int
    for i,_ := range board{
        for j , _ := range board[0]{
            flag= backtrack(0,word, board, [2]int{i,j},&visited)
            if flag{
                return true
            }
        }
    }
    return false
}
    func backtrack(i int, word string, board [][]byte, curr [2]int,visited *[][2]int)bool{
    if contains(curr,visited){
        return false
    }
    if board[curr[0]][curr[1]] != word[i] {
    return false
    }

    if i == len(word)-1 {
        return true
    }
    if board[curr[0]][curr[1]]==word[i]{
        *visited = append(*visited,curr)
       flag:=false
       poss:=[4][2]int{{0,1},{1,0},{-1,0},{0,-1}}
       
        for _ , add := range poss{
            lookAhead:=[2]int { curr[0]+add[0], curr[1]+ add[1]}
            if inBoard(lookAhead,board){
                flag = backtrack(i+1,word,board,lookAhead,visited)
            }
            if flag{
                return true
            }
        }
    }
    *visited= (*visited)[:len(*visited)-1]
    return false
}
func inBoard(ind [2]int,board [][]byte) bool {
    if ind[0]<0 || ind [0]>= len(board)|| ind[1]<0 || ind [1]>= len(board[0]){
        return false
    }
    return true
}
func contains(x [2]int, y *[][2]int)bool{
    for _ , iter := range *y {
        if x == iter{
            return true
        }
    }
    return false
}
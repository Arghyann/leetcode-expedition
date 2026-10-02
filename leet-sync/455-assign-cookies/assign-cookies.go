func findContentChildren(g []int, s []int) int {
    i:=0
    j:=0
    sort.Ints(s)
    sort.Ints(g)
    for i !=len(g)&&j!=len(s){
        if s[j]>=g[i]{
            i+=1
            j+=1
        }else{
            j+=1
        }
    }
    return i
}
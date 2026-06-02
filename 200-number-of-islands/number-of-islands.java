class Solution {
    private HashSet<String> set = new HashSet<>();
    public int numIslands(char[][] grid) {       
       int counter=0;
       for(int i =0;i<grid.length;i++){
        for(int j = 0;j<grid[0].length;j++){
            String s=""+i+","+j;
            if(grid[i][j]=='0' || set.contains(s)){
                continue;                
            }
            else{
                counter++;
                dfs(i,j,grid);
            }

        }
       } 
       return counter;
    }
    private void dfs(int i,int j,char[][] grid){
        String s =""+i+","+j;
        if(grid[i][j]=='0' || set.contains(s)){
            return;
        }        
        set.add(s);
        for(int ni=-1;ni<=1;ni++){
            for(int nj = -1;nj<=1;nj++){
                if(Math.abs(ni)==Math.abs(nj)){
                    continue;
                }
                if(i+ni >= 0 && i+ni < grid.length &&
            j+nj >= 0 && j+nj < grid[0].length){
                dfs(i+ni,j+nj,grid);
            }
            }
        }
        return;
    }
}
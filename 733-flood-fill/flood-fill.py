class Solution(object):
    
    def dfs(self,i,j,new_color,inital_color,vis,r,cols):
        if i<0 or i>=r or j<0 or j>=cols:
            return
        if vis[i][j]!=inital_color:
            return
        vis[i][j]=new_color
        
        self.dfs(i + 1, j, new_color, inital_color, vis, r, cols)
        self.dfs(i, j - 1, new_color, inital_color, vis, r, cols)
        self.dfs(i - 1, j, new_color, inital_color, vis, r, cols)
        self.dfs(i, j + 1, new_color, inital_color, vis, r, cols)

    def floodFill(self, image, sr, sc, color):
        if image[sr][sc]==color:
            return image
        vis=deepcopy(image)
        r=len(vis)
        cols=len(vis[0])
        inital_color=vis[sr][sc]
        self.dfs(sr,sc,color,inital_color,vis,r,cols)
        return vis

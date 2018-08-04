#include <hash_map>
#include <vector>
#include <unordered_map>
using namespace __gnu_cxx;
using namespace std;

class Solution {
public:
    int leastBricks(vector<vector<int>>& wall) {
        int height = wall.size();
        int tag = 0;
        unordered_map<int, int> map;
        for (int j=0; j<wall[0].size(); j++)
        	map[j] = 0;
        for (int i=0; i<height; i++){
        	int width = wall[i].size();
        	if (width != 1)
        		tag = 1;
        	int position = 0;
        	for (int j = 0; j < width-1; j++){
        		position += wall[i][j];
        		map[position] = map[position] + 1;
			}
		}
        if (tag == 0)
        	return height;
        int max = INT_MIN;
        for (auto& iter: map){
        	if (iter.second > max)
        		max = iter.second;
		}
		return height-max;
    }
};

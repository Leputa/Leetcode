#include <vector>
using namespace std;

class Solution {

private:
    int ret=0;
    void mergeSort(vector<int> &data, int lo, int hi){
        if (lo >= hi)
            return;

        int mid = (lo + hi) / 2;
        mergeSort(data, lo, mid);
        mergeSort(data, mid+1, hi);
        merge(data, lo, hi, mid);
    }

    void merge(vector<int> &data, int lo, int hi, int mid){
        vector<int>aux = data;

        int i=lo, j=mid+1, k=lo;
        while(i<=mid && j<=hi){
            if (aux[i] <= aux[j])
                data[k++] = aux[i++];
            else{
                // 前面的比后面的大， 构成逆序对
                // i到mid有序，[i, mid]j均与j构成逆序对
                data[k++] = aux[j++];
                ret += mid - i + 1;
                ret %= 1000000007;
            }
        }
        while(i<=mid)
            data[k++] = aux[i++];
        while(j<=hi)
            data[k++] = aux[j++];
    }

public:
    int InversePairs(vector<int> data) {
        mergeSort(data, 0, data.size()-1);
        return ret;
    }
};
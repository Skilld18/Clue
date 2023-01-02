#ifndef CLUE_CARDS_H
#define CLUE_CARDS_H
#include <map>

const std::map<int, std::string> cards{
    {0, "Scarlett"},
    {1, "Plum"},
    {2, "Mustard"},
    {3, "White"},
    {4, "Peacock"},
    {5, "Green"},

    {6, "Wrench"},
    {7, "Rope"},
    {8, "Revolver"},
    {9, "Knife"},
    {10, "Candlestick"},
    {11, "Pipe"},

    {12, "Conservatory"},
    {13, "Lounge"},
    {14, "Billiard"},
    {15, "Kitchen"},
    {16, "Study"},
    {17, "Hall"},
    {18, "Dining"},
    {19, "Ballroom"},
    {20, "Library"},
};

std::map<int, std::string> leh;

//TODO::used check
std::string sub_lehmer(const long long combo)
{
    if (leh.size() > 0)
    {
        return leh[combo];
    }
    int count = 0;
    for (int i = 0;i<18;i++)
    {
        for (int j = i+1;j<18;j++)
        {
            for(int k = j+1;k<18;k++)
            {
                leh[count] = cards.at(i) + " " + cards.at(j) + " " + cards.at(k);
                count++;
            }
        }
    }
}

#endif //CLUE_CARDS_H

#include <iostream>
using namespace std;
bool*** get_pieces(int, int);
int count_mask(int, int, bool**);
bool** build_new_mask(int, int, bool***);
int main(void)
{
  int width, length;
  cin >> width >> length;
  auto b1 = get_pieces(width, length);
  auto b2 = build_new_mask(width, length, b1);
  auto out = count_mask(width, length, b2);
  cout << out << endl;
}
bool ** get_blank(int width, int length)
{
    bool** out = new bool*[length];
    for(int i = 0; i < length; i++)
        out[i] = new bool[length];
    return out;
}
void get_two_pieces(int width, int length, bool*** out)
{
  bool** buff1 = get_blank(width, length);
  bool** buff2 = get_blank(width, length);
  for(int i = 0; i < length; i++)
  {
    for(int j = 0; j < width; j++)
    {
      cin >> buff1[i][j];
      cin >> buff2[i][j + width];
    }
  }
  out[0] = buff1;
  out[1] == buff2;
}
bool *** get_pieces(int width, int length)
{
    bool*** out = new bool**[4];
    get_two_pieces(width, length / 2,out);
    get_two_pieces(width, length / 2, out + 2);
    return out;
}
bool** build_new_mask(int width, int length, bool***layers)
{
    auto out = get_blank(width, length);
    for(int i = 0; i < length; i++)
    {
        for(int j = 0; j < width; j++)
        {
            out[i][j] = 1;
            for(int k = 0; k < 4; k++)
            {
                out[i][j] &= layers[k][i][j];
            }
        }
    }
    return out;
}
int count_mask(int width, int length, bool** mask)
{
    int out = 0;
    for(int i = 0; i < length; i++)
    {
        for(int j = 0; j < width; j++)
        {
            if(mask[i][j] == 1)
            {
                out++;
            }
        }
    }
    return out;
}
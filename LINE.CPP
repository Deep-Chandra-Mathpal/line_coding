# include <graphics.h>
# include <iostream.h>
# include <conio.h>
# include <string.h>
# include <dos.h>

int main()
{

   void encode(char *,char *, int, int, int, int);
   void draw(int ,int ,char *, int);

   char *bits; int len;
    clrscr();

    cout << "************Enter the bits(0s, 1s) (max 24 bits)************\n";

   do{
   cin >> bits; len = strlen(bits);
   if(len>24) cout << "SIZE limit exceed!!!!! :\n Re-Enter: ";
   }while(len>24);

   char *o_bits =new char[len]; char *e_bits =new char[len*2];
    strcpy(o_bits,bits);

   int gd=DETECT, gm, i, x, y;
   initgraph(&gd,&gm,"C:\\TURBOC3\\BGI");
   setcolor(GREEN);
   settextstyle(2 ,0,7);
   outtextxy(10,45, "Code");

   x = 174;
   for(i=0; i<len; i++, x+=20)
   {
     if(o_bits[i]=='1')
	outtextxy(x, 40, "1");
     else
	outtextxy(x, 40, "0");
   }

   x=170;
   y=80;

	 outtextxy(0,100, "NRZ - L");
	 encode(o_bits,e_bits,len,0,2,0);
	 draw(x,y,e_bits,len*2);
	 y+=60;

	 outtextxy(0,160, "NRZ - I");
	 encode(o_bits,e_bits,len,3,4,0);
	 draw(x,y,e_bits,len*2);
	 y+=60;

	 outtextxy(0,220, "Bipolar AMI");
	 encode(o_bits,e_bits,len,3,1,0);
	 draw(x,y,e_bits,len*2);
	 y+=60;

	 outtextxy(0,280, "Manchester");
	 encode(o_bits,e_bits,len,0,2,1);
	 draw(x,y,e_bits,len*2);

	 y+=60;

	 outtextxy(0,340, "D-Manchester");
	 encode(o_bits,e_bits,len,4,3,1);
	 draw(x,y,e_bits,len*2);
	 y+=60;

	 outtextxy(0,400, "PseudoTernary");
	 encode(o_bits,e_bits,len,1,3,0);
	 draw(x,y,e_bits,len*2);
	 y+=60;
	 getch();
	 closegraph();

   return 0;
}
void draw(int x, int y, char *data, int len)
{
   int curr_y, prev_y = y;

   for(int i=0; i<len; i++, x+=10)
   {
       if(data[i]=='2') curr_y = y;
       if(data[i]=='1') curr_y = y+20;
       if(data[i]=='0')  curr_y = y+40;
	line(x,curr_y,x+10,curr_y);
	delay(20);

       if(prev_y != curr_y) line(x,prev_y,x,curr_y);
	delay(20);
	prev_y = curr_y;
      delay(50);
   }
   return;
}

void encode(char *o_data,char *e_data,int len,int one,int zero, int mid)
{
   int i, j, previous=2;

   for(i=0, j=0; i<len; i++, j+=2)
   {
      if(o_data[i]=='1')
      {
	 if(one==0)  e_data[j]='0';
	 if(one==1)  e_data[j]='1';
	 if(one==2)  e_data[j]='2';
	 if(one==3)
	 {
	   if(previous==2)
	   {
	     previous=0;
	     e_data[j]='0';
	   }
	   else
	   {
	     previous=2;
	     e_data[j]='2';
	   }
	 }
	 if(one==4)
	 {
	   if(previous==2) e_data[j]='2';
	   else e_data[j]='0';
	 }
      }
      else
      {
	 if(zero==0)    e_data[j]='0';
	 if(zero==1)    e_data[j]='1';
	 if(zero==2)    e_data[j]='2';
	 if(zero==3)
	 {
	   if(previous==2)
	   { previous=0; e_data[j]='0'; }
	   else
	   { previous=2;  e_data[j]='2'; }
	 }
	 if(zero==4)
	 {
	   if(previous==2)  e_data[j]='2';
	   else  e_data[j]='0';
	 }
      }
      if(mid==1)
      {
      if(e_data[j]=='2') e_data[j+1]='0';
	 else            e_data[j+1]='2';
	 if(previous==2) previous=0;
	 else            previous=2;
      }
      else e_data[j+1]=e_data[j];
   }
   return;
}


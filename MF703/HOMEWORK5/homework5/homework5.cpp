#include <iostream>
#include <cmath>
using namespace std;


double price(double year, double yield,double cpr){
    double coupon = 0.0;

    for(int i=1;i<=year;i++){
        coupon += cpr * pow(1+yield,-i);
    }
    double priceone = 100 / pow((1+yield),year);
    priceone += coupon;
    return priceone;
}

double duration2(double year, double yield,double cpr) {
    double cpfac = 0.0;

    for (int i = 1; i <= year; i++) {
        cpfac += cpr * pow(1 + yield, -i) * i;

    }
    double bdfac = year * 100 / pow((1 + yield), year);
    double d = bdfac + cpfac;
    double p1 = price(year, yield, cpr);

    return d / p1;
}

double duration(double year, double yield, double cpr){
    double d =  (price(year,yield-0.0000001,cpr) - price(year,yield+0.0000001,cpr)) / 0.0000002;
    double p1 = price(year,yield,cpr);

    return d / p1;

}
double convexity2(double year, double yield, double cpr){
    double cpcfac = 0.0;

    for (int i = 1; i <= year; i++) {
        cpcfac += cpr * pow(1 + yield, -i) * (i + i*i) ;

    }
    double bdcfac = (year+ year*year) * 100 / pow((1 + yield), year);
    double c = (bdcfac+cpcfac)/((1+yield)*(1+yield));
    double pricec = price(year,yield,cpr);

    return c / pricec;

}

double convexity(double year, double yield, double cpr){
    double c =  (price(year,yield+0.0000001,cpr) - 2 * price(year,yield,cpr) + price(year,yield-0.0000001,cpr)) / (0.0000001 * 0.0000001);
    double p1 = price(year,yield,cpr);
    return c / p1;

}
double convexity3(double year, double yield, double cpr){
    double c = (duration(year,yield,cpr)-duration(year,yield+0.001,cpr)) / 0.001;
    double p1 = duration(year, yield, cpr);
    return c / p1;
}


double adjustnum(){
    double cpr = 0.0;
    double yield1=0.025;
    double yield2=0.026;
    double yield3=0.027;
    double year1=1;
    double year2=2;
    double year3=3;

    double upper = 2;
    double lower = -2;
    double adj = 0;
    double durationew = 0.0;

    for (;1>0;){
        double portfolio = price(year1,yield1,cpr) + price(year3,yield3,cpr) - adj * price(year2,yield2,cpr);
        double p1 = price(year1,yield1,cpr)/portfolio;
        double p2 = adj * price(year2,yield2,cpr)/portfolio;
        double p3 = price(year3,yield3,cpr)/portfolio;

        durationew = p1 *duration(year1,yield1,cpr) + p3 *duration(year3,yield3,cpr) - p2 * duration(year2,yield2,cpr);
        if (durationew > 0){
            lower = adj;
        }

        if (durationew < 0){
            upper = adj;
        }
        adj = (lower + upper)/2;

        if (abs(durationew) < 0.0000001){
            break;
        }
    }
    return adj;

}








double * cashflow(){
    double cf[5];

    for (int i = 0; i < 5; i++) {
        cf[i] = 20 + (100 - i * double(20)) * 0.03;
    }
    return cf;
}

double amoprice(double ytm) {
    double price = 0;
    for (int i = 0; i < 5; i++) {
        price += *(cashflow() + i ) / pow((1+ytm),i+1);

    }
    return price;
}

double amoduration(double ytm) {
    return (amoprice(ytm + 0.0000001) - amoprice(ytm-0.0000001)) / (-0.0000002)  / amoprice(ytm);
}













//(a) Calculate prices of a zero coupon bond that pays $100 at maturity for each maturity & yield combination
void a(){
    cout<<"The result of problem a : \n";
    double cpr = 0.0;
    double yield[6] = {0.025,0.026,0.027,0.03,0.035,0.04};
    double year[6] = {1.0,2.0,3.0,5.0,10.0,30.0};
    for (int i=0 ; i < 6; i++){
        double p = price(year[i],yield[i],cpr);
        cout << " The price of a "<< year[i] <<" year(s) zero coupon bond with an yield-to-maturity of "<<yield[i] <<" is "<<p<<"\n";

    }
cout<<"\n";
}



//(b) Calculate the duration of each zero coupon bond, or sensitivity of the bond price to a change in bond yield,  using finite differences
void b(){
    double cpr = 0;
    cout<<"The result of problem b : \n";
    double yield[6] = {0.025,0.026,0.027,0.03,0.035,0.04};
    double year[6] = {1.0,2.0,3.0,5.0,10.0,30.0};
    for (int i=0 ; i < 6; i++){
        double p = duration(year[i],yield[i],cpr);
        cout << " The duration of a "<< year[i] <<" year(s) coupon bond that pay $100 at maturity at 3% annually with an yield-to-maturity of "<<yield[i] <<" is "<<p<<"\n";

    }
    cout<<"\n";
}




//(c) Calculate prices of coupon bonds that pay $100 at maturity at 3% annually until maturity.
void c(){
    cout<<"The result of problem c : \n";
    double cpr = 3;
    double yield[6] = {0.025,0.026,0.027,0.03,0.035,0.04};
    double year[6] = {1.0,2.0,3.0,5.0,10.0,30.0};
    for (int i=0 ; i < 6; i++){
        double p = price(year[i],yield[i],cpr);
        cout << " The price of a "<< year[i] <<" year(s) coupon bond that pay $100 at maturity at 3% annually until maturity with an yield-to-maturity of "<<yield[i] <<" is "<<p<<"\n";

    }
    cout<<"\n";
}


//(d) Calculate the duration of each coupon bond using finite differences.
void d(){
    double cpr = 3;
    cout<<"The result of problem d : \n";
    double yield[6] = {0.025,0.026,0.027,0.03,0.035,0.04};
    double year[6] = {1.0,2.0,3.0,5.0,10.0,30.0};
    for (int i=0 ; i < 6; i++){
        double p = duration(year[i],yield[i],cpr);
        cout << " The duration of a "<< year[i] <<" year(s) coupon bond that pay $100 at maturity at 3% annually with an yield-to-maturity of "<<yield[i] <<" is "<<p<<"\n";

    }
    cout<<"\n";
}

//（e）Calculate the second derivative of each bond price with respect to yield (commonly known as convexity)
void e(){
    double cpr = 3;
    cout<<"The result of problem e : \n";
    double yield[6] = {0.025,0.026,0.027,0.03,0.035,0.04};
    double year[6] = {1.0,2.0,3.0,5.0,10.0,30.0};
    for (int i=0 ; i < 6; i++){
        double p = convexity(year[i],yield[i],cpr);
        cout << " The convexity of a "<< year[i] <<" year(s) coupon bond that pay $100 at maturity at 3% annually with an yield-to-maturity of "<<yield[i] <<" is "<<p<<"\n";

    }
    cout<<"\n";

}


//(f)Consider a portfolio that is long one unit of the 1 year zero-coupon bond, long one unit of the 3 year zero-coupon bond and short two units of the 2 year zero-coupon bond. Calculate the initial value of the portfolio.
void f(){
    double cpr = 0.0;
    cout<<"The result of problem f : \n";
    double yield[3] = {0.025,0.026,0.027};
    double year[3] = {1.0,2.0,3.0};
    double portfolio = price(year[0],yield[0],cpr) + price(year[2],yield[2],cpr) - 2 * price(year[1],yield[1],cpr);
    cout << "The value of this portfolio is "<< portfolio<< ". \n";

}

//(g) Calculate the duration and the convexity of this portfolio.
void g(){
    double cpr = 0.0;
    cout << "The result of problem g : \n";
    double yield[3] = {0.025,0.026,0.027};
    double year[3] = {1.0,2.0,3.0};
    double portfolio = price(year[0],yield[0],cpr) + price(year[2],yield[2],cpr) - 2 * price(year[1],yield[1],cpr);
    double p1 = price(year[0],yield[0],cpr)/portfolio;
    double p2 = 2 * price(year[1],yield[1],cpr)/portfolio;
    double p3 = price(year[2],yield[2],cpr)/portfolio;

    double durationp = p1 *duration(year[0],yield[0],cpr) + p3 *duration(year[2],yield[2],cpr) - p2 * duration(year[1],yield[1],cpr);
    cout << " The duration of this portfolio is "<< durationp <<". \n";
    double covexp = p1 * convexity(year[0],yield[0],cpr) + p3 * convexity(year[2],yield[2],cpr) - p2 * convexity(year[1],yield[1],cpr);
    cout << " The convexity of this portfolio is "<< covexp <<".\n";

}

void hij(){
    double cpr = 0.0;
    cout << "The result of problem h : \n";
    double yield[3] = {0.025,0.026,0.027};
    double year[3] = {1.0,2.0,3.0};
    double portfolio = price(year[0],yield[0],cpr) + price(year[2],yield[2],cpr) + 2 * price(year[1],yield[1],cpr);
    double number = adjustnum(); ///use dichotomy to find the adjust number.
    cout << " The units required to do this : "<< number <<". \n";
    cout << "The result of problem i : \n";
    double changein = (price(year[0],yield[0]+0.01,cpr)+ price(year[2],yield[2]+0.01,cpr) - number * price(year[1],yield[1]+0.01,cpr)-(price(year[0],yield[0],cpr)+ price(year[2],yield[2],cpr) - number * price(year[1],yield[1],cpr)));
    cout << " The change happened to the portfolio  : "<< changein <<". \n";
    cout<<"\n"<<price(year[0],yield[0]+0.01,cpr)+ price(year[2],yield[2]+0.01,cpr)- number * price(year[1],yield[1]+0.01,cpr)<<"\n";


    cout << "The result of problem j : \n";
    double changede = (price(year[0],yield[0]-0.01,cpr)+ price(year[2],yield[2]-0.01,cpr) - number * price(year[1],yield[1]-0.01,cpr)-(price(year[0],yield[0],cpr)+ price(year[2],yield[2],cpr) - number * price(year[1],yield[1],cpr)))
                      ;
    cout << " The change happened to the portfolio  : "<< changede <<". \n";

}



void k(){
    cout << "The result of problem k : \n";
    cout << " The results are shown below  : "<< *cashflow()<<" "<< *(1+cashflow())<<" "<<*(2+cashflow())<<" "<<*(3+cashflow())<<" "<<*(4+cashflow())<<"\n";
}



void l() {
    cout <<"The result of problem l : \n"<<"price: " <<amoprice(0.03) <<"\n";
    cout << "Duration: " << amoduration(0.03) << endl;
}






int main() {
    a();
    b();
    c();
    d();
    e();
    f();
    g();
    hij();
    k();
    l();



    return 0;
}

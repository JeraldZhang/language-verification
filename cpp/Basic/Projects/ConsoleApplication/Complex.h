#pragma once
class Complex
{
public:
	Complex(double r = 0, double i = 0)
		:re(r), im(i) {
		re = r;
		im = i;
	};
	~Complex();
	Complex& operator += (const Complex&);
	double real() const { return re; }
	double imag() const { return im; }
private:
	double re, im;
	friend Complex& __doapl(Complex*, const Complex&);
};

Complex::Complex(double r = 0, double i = 0)
{
}

Complex::~Complex()
{
}
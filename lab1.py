{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Q1: User input a string \"A\" and \"B\" having with length 10 and 5 res\n",
    "#Q2 : Convert String A to upper case"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10\n",
      "5\n"
     ]
    }
   ],
   "source": [
    "#q1\n",
    "A=\"0123456789\"\n",
    "B=\"12345\"\n",
    "print(len(A))\n",
    "print(len(B))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "NEHIL\n"
     ]
    }
   ],
   "source": [
    "A=\"nEHiL\"\n",
    "print(A.upper())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Q3: Create script to input two numbers x and y with following instruction:\n",
    "#add when user select 1, sub on 2, mul on 3, div 4 and power on 5(give options to select x^y or y^x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter 1st number 2\n",
      "Enter 2nd number 3\n",
      "Enter your selection 5\n",
      "select 1 to execute '2^3' OR select 2 to execute '3^2'1\n",
      "8\n"
     ]
    }
   ],
   "source": [
    "a=int(input(\"Enter 1st number \"))\n",
    "b=int(input(\"Enter 2nd number \"))\n",
    "c=int(input(\"Enter your selection \"))\n",
    "if c==1:\n",
    "    print(a+b)\n",
    "elif c==2:\n",
    "    print(a-b)\n",
    "elif c==3:\n",
    "    print(a*b)\n",
    "elif c==4:\n",
    "    print(a/b)\n",
    "elif c==5:\n",
    "    d=int(input((\"select 1 to execute '%d^%d' OR select 2 to execute '%d^%d'\" %(a,b,b,a))))\n",
    "    if d==1:\n",
    "        print(a**b)\n",
    "    elif d==2:\n",
    "        print(b**a)\n",
    "    else:\n",
    "        print(\"Not a valid entry, please retry whole program\")\n",
    "else:\n",
    "    print(\"Not a valid entry, please retry whole program\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

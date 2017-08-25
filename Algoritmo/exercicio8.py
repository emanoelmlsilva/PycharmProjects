"""Faça um algoritmo que leia a idade de uma pessoa expressa em dias e mostre-a expressa em
anos, meses e dias."""

idade_dias = int(input('Informe a idade expressada em dias: '))
anos = idade_dias/365
mes = (idade_dias%365)/30
dias = (idade_dias%365)%30

print('%d anos, %d meses, %d dias '%(anos,mes,dias))
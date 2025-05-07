/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.Laboratorio2;

/**
 *
 * @author Usuario
 */
public class Fecha {

    private int dd;
    private int mm;
    private int aa;
    public Fecha(){
        dd=0;
        mm=0;
        aa=0;
    }
    public Fecha(int dd, int mm, int aa){
        this.dd = dd;
        this.mm = mm;
        this.aa = aa;
    }
    public int getDia(){
        return dd;
    }
    
    public int getMes(){
        return mm;
    }
    
    public int getAño(){
        return aa;
    }
    
    public void setDia(int dd){
        this.dd=dd;
    }
    
    public void setMes(int mm){
        this.mm=mm;
    }
    
    public void setAño(int aa){
        this.aa=aa;
    }
    
    public String toStr(){
        return dd + "/" + mm + "/" + aa;  
    }
}



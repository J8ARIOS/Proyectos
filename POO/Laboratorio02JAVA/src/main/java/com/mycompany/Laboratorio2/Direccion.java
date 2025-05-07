/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.Laboratorio2;

/**
 *
 * @author Usuario
 */
public class Direccion {
    private String calle;
    private String nomenclatura;
    private String barrio;
    private String ciudad;
    private String edificio;
    private String apto;
    public Direccion(){
    }
    public Direccion(String calle, String nomenclatura, String barrio, String ciudad, String edificio, String apto){
        
        this.calle = calle;
        this.nomenclatura = nomenclatura;
        this.barrio = barrio;
        this.ciudad = ciudad;
        this.edificio = edificio;
        this.apto = apto;
    }
    public void setCalle(String calle){
        this.calle = calle;
    } 
    public void setNomenclatura(String nomenclatura){
        this.nomenclatura = nomenclatura;
    }
    public void setBarrio(String barrio){
        this.barrio = barrio;
    }
    public void setCiudad(String ciudad){
        this.ciudad = ciudad;
    }
    public void setEdificio(String edificio){
        this.edificio = edificio;
    }
    public void setApto(String apto){
        this.apto = apto;
    }
    public String getCalle(){
        return calle;
    }
    public String getNomenclatura(){
        return nomenclatura;
    }
    public String getCiudad(){
        return ciudad;
    }
    public String getBarrio(){
        return barrio;
    }
    public String getEdificio(){
        return edificio;
    }
    public String getApto(){
        return apto;
    }
    public String toStr(){
        return "\nCalle: " + calle  + 
               "\nNomenclatura: " + nomenclatura + 
               "\nCiudad: " + ciudad + 
               "\nBarrio: " + barrio + 
               "\nEdificio: " + edificio + 
               "\nApto: " + apto;  
    }  
}

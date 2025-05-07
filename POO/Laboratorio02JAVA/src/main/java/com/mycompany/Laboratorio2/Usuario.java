/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.Laboratorio2;

/**
 *
 * @author Usuario
 */
public class Usuario{
    private String nombre;
    private long ID;
    private String fecha_nacimiento;
    private String ciudad_nacimiento;
    private long telefono;
    private String email;
    private String direccion;
    public Usuario(){
    }
    public Usuario(String nombre, long ID, String fecha_nacimiento, String ciudad_nacimiento, long telefono, String email, String direccion){
        this.nombre = nombre;
        this.ID = ID;
        this.fecha_nacimiento = fecha_nacimiento;
        this.ciudad_nacimiento = ciudad_nacimiento;
        this.telefono = telefono;
        this.email = email;
        this.direccion = direccion;
    }
    //Gettings
    public String getName(){
        return nombre;
    }
    public long getID(){
        return ID;
    }
    public String getFecha_nacimiento(){
        return fecha_nacimiento;
    }
    public String getCiudad_nacimiento(){
        return ciudad_nacimiento;
    }
    public long getTelefono(){
        return telefono;
    }
    public String getEmail(){
        return email;
    }
    public String getDireccion(){
        return direccion;
    }
    //Settings
    public void setNombre(String nombre){
        this.nombre = nombre;
    }
    public void setID(long ID){
        this.ID = ID;
    }
    public void setFecha_nacimiento(String fecha_nacimiento){
        this.fecha_nacimiento = fecha_nacimiento;
    }
    public void setCiudad_nacimiento(String ciudad_nacimiento){
        this.ciudad_nacimiento = ciudad_nacimiento;
    }
    public void setTelefono(long telefono){
        this.telefono = telefono;
    }
    public void setEmail(String email){
        this.email = email;
    }
    public void setDireccion(String direccion){
        this.direccion = direccion;
    }
    public String toStr(){
        return "\nNombre: " + nombre + "\n" +
                "ID: " + ID + "\n" +
                "Fecha de nacimiento: " + fecha_nacimiento + "\n" +
                "Ciudad de nacimiento: " + ciudad_nacimiento + "\n" +
                "Telefono: " + telefono + "\n" +
                "E-mail: " + email + "\n" +
                "Direccion de residencia: " + direccion;
    }
}


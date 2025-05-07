/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.Laboratorio2;

/**
 *
 * @author Usuario
 */
import java.util.Scanner;
public class Laboratorio02{
        public static void main(String[] args) {
            Scanner input = new Scanner(System.in);

            Fecha fecha_nac = new Fecha();
            fecha_nac.setDia(23);
            fecha_nac.setMes(07);
            fecha_nac.setAño(2006);
            System.out.println(fecha_nac.toStr());
            
            Direccion direccion1 = new Direccion();
            direccion1.setCalle("Calle 10");
            direccion1.setNomenclatura("No. 20-30");
            direccion1.setBarrio("Centro");
            direccion1.setCiudad("Medellin");
            direccion1.setEdificio("Torre Norte");
            direccion1.setApto("101");
            System.out.println(direccion1.toStr());
            
            Usuario usuario1 = new Usuario();
            usuario1.setNombre("Ana");
            usuario1.setID(123456789L);
            usuario1.setFecha_nacimiento(fecha_nac.toStr());
            usuario1.setCiudad_nacimiento("Bogota");
            usuario1.setTelefono(3001234567L);
            usuario1.setEmail("ana@example.com");
            usuario1.setDireccion(direccion1.toStr());
            System.out.println(usuario1.toStr());
            
            Fecha fecha_usuario2 = new Fecha();
            System.out.print("\nIngrese su dia de nacimiento: ");
            int dia = input.nextInt();
            System.out.print("\nIngrese el numero del mes de su nacimiento: ");
            int mes = input.nextInt();
            System.out.print("\nIngrese su año de nacimiento: ");
            int año = input.nextInt();
            fecha_usuario2.setDia(dia);
            fecha_usuario2.setMes(mes);
            fecha_usuario2.setAño(año);
            input.nextLine();
            
            Usuario usuario2 = new Usuario();
            
            System.out.print("\nIngrese su nombre: ");
            String nombre = input.nextLine();
            usuario2.setNombre(nombre);
            
            System.out.print("Ingrese su ID: ");
            long ID = input.nextLong();
            usuario2.setID(ID);
            
            input.nextLine();

            usuario2.setFecha_nacimiento(fecha_usuario2.toStr());
             
            System.out.print("Ingrese su ciudad de nacimiento: ");
            String ciudad_nacimiento = input.nextLine();
            usuario2.setCiudad_nacimiento(ciudad_nacimiento);
             
            System.out.print("Ingrese su numero de telefono: ");
            long telefono = input.nextLong();
            usuario2.setTelefono(telefono);
            
            input.nextLine();
            
            System.out.print("Ingrese su Email: ");
            String email = input.nextLine();
            usuario2.setEmail(email);

            Direccion direccion_usuario2 = new Direccion();
            System.out.print("\nIngrese la calle: ");
            String calle = input.nextLine();
            System.out.print("\nIngrese la nomenclatura: ");
            String nomenclatura = input.nextLine();
            System.out.print("\nIngrese el barrio: ");
            String barrio = input.nextLine();
            System.out.print("\nIngrese la ciudad: ");
            String ciudad = input.nextLine();
            System.out.print("\nIngrese el edificio: ");
            String edificio = input.nextLine();
            System.out.print("\nIngrese el apartamento: ");
            String apto = input.nextLine();

            direccion_usuario2.setCalle(calle);
            direccion_usuario2.setNomenclatura(nomenclatura);
            direccion_usuario2.setBarrio(barrio);
            direccion_usuario2.setCiudad(ciudad);
            direccion_usuario2.setEdificio(edificio);
            direccion_usuario2.setApto(apto);

             usuario2.setDireccion(direccion_usuario2.toStr());
            
            System.out.println(usuario2.toStr());
    }
}






    


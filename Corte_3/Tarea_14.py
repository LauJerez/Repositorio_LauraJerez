class articulos():
    def _init_(self, nombre: str, precio: int):
        self.producto=nombre
        self.preciop=precio

    def get_producto(self):
        return self.producto
    
    def get_preciop(self):
        return self.preciop
    
    def set_nombre(self,nombre):
        self.nombre=nombre

    def set_nombre(self,precio):
        self.preciop=precio

#---------------Clase Hijo Pan---------------

class pan(articulos):
    def _init_(self, nombre: str, precio: int, IVA= int):
        super()._init_(nombre, precio)

        self.valor_iva=IVA

    def get_valor_iva(self):
        return self.valor_iva

    def set_preciop(self, IVA):
        self.valor_iva=IVA

    def iva(self):
        if self.get_valor_iva() == 0 :
            return 'El producto no incluye el valor del IVA.'
        else:
            return f'El producto tiene un IVA del {self.get_valor_iva()}%.'
        
#---------------Clase Hijo Chocolate---------------

class chocolate(articulos):
    def _init_(self, nombre: str, precio: int, IVA= int):
        super()._init_(nombre, precio)

        self.valor_iva=IVA

    def get_valor_iva(self):
        return self.valor_iva

    def set_preciop(self, IVA):
        self.valor_iva=IVA

    def iva(self):
        if self.get_valor_iva() == 0.05 or self.get_valor_iva() == 5:
             vn=self.preciop/1.05
             vb=vn*1.05
             iva=vn*0.05
             return f'El valor brtuto del producto es: valor neto={vn} + el iva={iva} -----> valor bruto: {vb} '
        else:
            return f'El producto tiene un IVA del {self.get_valor_iva()}%.'

#---------------Clase Hijo Ropa---------------

class ropa(articulos):
    def _init_(self, nombre: str, precio: int, IVA= int):
        super()._init_(nombre, precio)

        self.valor_iva=IVA

    def get_valor_iva(self):
        return self.valor_iva

    def set_preciop(self, IVA):
        self.valor_iva=IVA

    def iva(self):
        if self.get_valor_iva() == 0.19 or self.get_valor_iva() == 19:
             vn=self.preciop/1.19
             vb=vn*1.19
             iva=vn*0.19
             return f'El valor brtuto del producto es: valor neto={vn} + el iva={iva} -----> valor bruto: {vb} '
        else:
            return f'El producto tiene un IVA del {self.get_valor_iva()}%.'

def main():
    art = articulos('Azucar', 300)
    art1= pan('Pan', 200, 0)
    art2=chocolate('Chocolate', 50000, 5)
    art3=ropa('Zapatos Air Force 1', 450000, 19)

    print(f'\n\n\n\n\nProducto: {art.get_producto()}, Precio: {art.get_preciop()}')

    print('----------------------------------------------')

    print(f'Producto: {art1.get_producto()}, Precio: {art1.get_preciop()}, iva: {art1.get_valor_iva()}%')
    print(f'{art1.iva()}\n')
    print('----------------------------------------------')

    print(f'Producto: {art2.get_producto()}, Precio: {art2.get_preciop()}, iva: {art2.get_valor_iva()}%')
    print(f'{art2.iva()}\n')
    print('----------------------------------------------')

    print(f'Producto: {art3.get_producto()}, Precio: {art3.get_preciop()}, iva: {art3.get_valor_iva()}%')
    print(f'{art3.iva()}\n\n\n\n\n')
    
if __name__=='__main__':
    main()
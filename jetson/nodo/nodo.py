import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool

class NodoSensor(Node):

    def __init__(self):
        super().__init__('nodo_sensor')
        self.publisher = self.create_publisher(Bool, '/sensor_status', 10)
        self.timer = self.create_timer(0.1, self.publicar)
        self.get_logger().info('Nodo sensor iniciado')

    def publicar(self):
        mensaje = Bool()
        mensaje.data = True  # esto vendrá del STM32
        self.publisher.publish(mensaje)

def main():
    rclpy.init()
    nodo = NodoSensor()
    rclpy.spin(nodo)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
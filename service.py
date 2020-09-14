from src.views.customers import *
from src.views.orders import createorder,delete_order
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1234, debug=True)

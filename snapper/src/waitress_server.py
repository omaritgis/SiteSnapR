from waitress import serve
import middleware

serve(middleware.app, host='127.0.0.1', port=80)
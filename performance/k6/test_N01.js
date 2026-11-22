
import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
    vus: 5,
    duration: '30s',

    thresholds: {
        http_req_duration: ['p(95)<2000'],
        http_req_failed: ['rate<0.01'],
        checks: ['rate>0.99']
    }
};

export default function () {

    const respuesta = http.get(
        'http://localhost:5000/api/products'
    );

    check(respuesta, {
        'Codigo HTTP 200': (r) => r.status === 200,
        'Respuesta no vacia': (r) => r.body.length > 0
    });

    sleep(1);
}

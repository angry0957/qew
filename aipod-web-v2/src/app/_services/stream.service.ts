import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class StreamService {

  URL = 'http://localhost:5005/';
  constructor(private http: HttpClient) { }

  changeSource(sourceId) {
    return this.http.get(this.URL + 'setsource?source=' + sourceId)
  }
}

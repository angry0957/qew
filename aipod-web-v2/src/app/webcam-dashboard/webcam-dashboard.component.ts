import { Component } from '@angular/core';
import { StreamService } from 'app/_services/stream.service';

export enum ObservableType {
  weapons = 'weapons',
  vehicle = 'vehicle',
  objects = 'objects',
  face = 'face',
  sentiment = 'sentiment'
}

@Component({
  selector: 'app-webcam-dashboard',
  templateUrl: './webcam-dashboard.component.html',
  styleUrls: ['./webcam-dashboard.component.css']
})
export class WebcamDashboardComponent {

  constructor(private streamService: StreamService) {}
  videoSource: number = 1;
  selectType: ObservableType = ObservableType.objects;
  type = ObservableType;

  todayDate: any = new Date();
  time = this.todayDate.getHours() + ':' + this.todayDate.getMinutes() + ':' + this.todayDate.getSeconds();

  rand() {
    return Math.random();
  }

  changeSource(source) {
    this.videoSource = source;
    this.streamService.changeSource(source)
  }

  changeModel(model) {
    this.selectType = model;
    (<HTMLImageElement>document.getElementById('video-img')).src = 'http://83.110.154.229:5005/video?source=' + this.videoSource + '&type=' + model + '&rand=' + this.rand();
  }
  
  detectedFaces: any[] = [{
    firstName: 'Target',
    lastName: '',
    photo: './assets/img/placeholder1.jpg',
    gender: '',
    dateOfBirth: '',
    placeOfBirth: '',
    nationality: 'Nationality',
    wantedStatus: 0,
    wantedBy: '',
    charge: '',
    timeStamp: 'Time'
  }, {
    firstName: 'Target',
    lastName: '',
    photo: './assets/img/placeholder1.jpg',
    gender: '',
    dateOfBirth: '',
    placeOfBirth: '',
    nationality: 'Nationality',
    wantedStatus: 0,
    wantedBy: '',
    charge: '',
    timeStamp: 'Time'
  }, {
    firstName: 'Target',
    lastName: '',
    photo: './assets/img/placeholder1.jpg',
    gender: '',
    dateOfBirth: '',
    placeOfBirth: '',
    nationality: 'Nationality',
    wantedStatus: 0,
    wantedBy: '',
    charge: '',
    timeStamp: 'Time'
  }, {
    firstName: 'Target',
    lastName: '',
    photo: './assets/img/placeholder1.jpg',
    gender: '',
    dateOfBirth: '',
    placeOfBirth: '',
    nationality: 'Nationality',
    wantedStatus: 0,
    wantedBy: '',
    charge: '',
    timeStamp: 'Time'
  }];

  detectedObjects: any[] = [{
    objectDetected: 'Target',
    confidence: 0,
    timeFrame: this.time
  }, {
    objectDetected: 'Target',
    confidence: 0,
    timeFrame: this.time
  }, {
    objectDetected: 'Target',
    confidence: 0,
    timeFrame: this.time
  }, {
    objectDetected: 'Target',
    confidence: 0,
    timeFrame: this.time
  }];
}

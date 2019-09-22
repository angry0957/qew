import { Component, EventEmitter, OnInit, Output } from '@angular/core';

@Component({
  selector: 'app-camera-list',
  templateUrl: './camera-list.component.html',
  styleUrls: ['./camera-list.component.css']
})
export class CameraListComponent implements OnInit {

  @Output() changeSource = new EventEmitter();

  source: any;
  feedName = ['Recorded 1', 'Local', 'Handheld AUX', 'Drone 1', 'Drone 2', 'Drone 3', 'Drone 4', 'Drone 5'];
  sourceImage = ['vid-record', 'local', 'aux1', 'drone4', 'drone4', 'drone4', 'drone4', 'drone4'];

  constructor() {
  }

  ngOnInit() {
  }

  setSource(source) {
    this.source = source !== this.source ? source : 0;
    this.changeSource.emit(this.source);
  }

}





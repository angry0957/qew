import { Component, EventEmitter, Input, Output } from '@angular/core';
import { StreamService } from 'app/_services/stream.service';

declare var changeStreamById: any;

@Component({
  selector: 'app-video-source',
  templateUrl: './video-source.component.html',
  styleUrls: ['./video-source.component.css']
})
export class VideoSourceComponent {

  @Output() changeSource = new EventEmitter();
  @Input() streamId;
  @Input() feedName;
  @Input() streamingStatus;
  @Input() sourceImage;

  constructor(private streamService: StreamService) {
  }

  changeStream(streamId) {
    this.streamService.changeSource(streamId).subscribe(result => {

    }, error => {
      alert('error in connection')
    })
  }
}

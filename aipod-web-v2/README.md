# AipodNgClient

This project was generated with [Angular CLI](https://github.com/angular/angular-cli) version 7.3.8.

## Development server

Run `ng serve` for a dev server. Navigate to `http://localhost:4200/`. The app will automatically reload if you change any of the source files.

## Code scaffolding

Run `ng generate component component-name` to generate a new component. You can also use `ng generate directive|pipe|service|class|guard|interface|enum|module`.

## Build

Run `ng build` to build the project. The build artifacts will be stored in the `dist/` directory. Use the `--prod` flag for a production build.

## Running unit tests

Run `ng test` to execute the unit tests via [Karma](https://karma-runner.github.io).

## Running end-to-end tests

Run `ng e2e` to execute the end-to-end tests via [Protractor](http://www.protractortest.org/).

## Further help

To get more help on the Angular CLI use `ng help` or go check out the [Angular CLI README](https://github.com/angular/angular-cli/blob/master/README.md).
"# aipod-ng-client" 


# Update NodeJS

    # Using Ubuntu
    curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
    sudo apt-get install -y nodejs

    ## Run `sudo apt-get install -y nodejs` to install Node.js 10.x and npm
    ## You may also need development tools to build native addons:
        sudo apt-get install gcc g++ make
    ## To install the Yarn package manager, run:
        curl -sL https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
        echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
        sudo apt-get update && sudo apt-get install yarn

# AWS EC2

https://medium.com/@sandeeptengale/deploy-angular-app-on-aws-ec2-instance-20749f17b33e

https://appdividend.com/2019/06/04/angular-8-tutorial-with-example-learn-angular-8-crud-from-scratch/


Add external js file in index.html.

<script src="./assets/vendors/myjs.js"></script>

Here's myjs.js file :

  var myExtObject = (function() {

      return {
        func1: function() {
          alert('function 1 called');
        },
        func2: function() {
          alert('function 2 called');
        }
      }

  })(myExtObject||{})


  var webGlObject = (function() { 
      return { 
        init: function() { 
          alert('webGlObject initialized');
        } 
      } 
  })(webGlObject||{})

Then declare it is in component like below

demo.component.ts

  declare var myExtObject: any;
  declare var webGlObject: any;

  constructor(){
      webGlObject.init();
  }

  callFunction1() {
      myExtObject.func1();
  }

  callFunction2() {
      myExtObject.func2();
  }

demo.component.html

<div>
    <p>click below buttons for function call</p>
    <button (click)="callFunction1()">Call Function 1</button>
    <button (click)="callFunction2()">Call Function 2</button>
</div>


gsutil rsync -r gs://aipod-web-bucket ./aipod-web



https://medium.com/@jkeung/integrating-google-maps-api-w-angular-7-e7672396ce2d



# Resets index to former commit; replace '56e05fced' with your commit code
git reset 56e05fced 

# Moves pointer back to previous HEAD
git reset --soft HEAD@{1}

git commit -m "Revert to 56e05fced"

# Updates working copy to reflect the new commit
git reset --hard


// console.log('detectFrameForWeapon:');
    // this.tensor = this.preprocessImage(this.video, "olga");
    // let tensor = this.tensor;
    // model.predict(tensor).data().then(predictions=>{

    //     // console.log(prediction);
    //     let top5=Array.from(predictions)
    //     .map(function(p,i){
    //       return {
    //         score: p,
    //         class: IMAGENET_CLASSES[i]
    //       };
    //     }).sort(function(a:any ,b:any){
    //       return b.score-a.score;
    //     }).slice(0,5);
    //     console.log(top5);

    //     const prediction:any = top5[0];

    //     const temp = this.detected_objects.findIndex((item:any) => item.objectDetected === prediction.class)
    //     console.log('TEMP')
    //     console.log(temp);
    //     var today = new Date();
    //     var time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
    //     if(temp === -1){
    //       this.detected_objects.push({
    //         objectDetected: prediction.class,
    //         confidence:Math.round(prediction.score*100),
    //         timeFrame: time
    //       });
    //     }else{
    //       this.detected_objects.splice(temp,1);

    //       this.detected_objects.push({
    //         objectDetected: prediction.class,
    //         confidence:Math.round(prediction.score*100),
    //         timeFrame: time
    //       });
    //      }
    //     if (this.detected_objects.length >20)
    //     {
    //       this.detected_objects.splice(0, this.detected_objects.length-20);
    //     }

    //   console.log('detectFrameForWeapon executed');
    //   requestAnimationFrame(() => {
    //     if (this.detectionMode !== 2) return;
    //     setTimeout(() => {this.detectFrameForWeapon(video, model);}, 300);
    //   });
    // });


 // "@tensorflow/tfjs": "^1.2.7",
        // "@tensorflow/tfjs-node": "latest",
        



tf.loadModel() is renamed to:
loadLayersModel(pathOrIOHandlerOrJSON: string|io.IOHandler|LayersModelJSON,
    options: LoadOptions): Promise<tf.LayersModel>;
tf.loadFrozenModel() is renamed to:
loadGraphModel(pathOrIOHandlerOrJSON: string|io.IOHandler|GraphModelJSON,
    options: LoadOptions): Promise<tf.GraphModel>;

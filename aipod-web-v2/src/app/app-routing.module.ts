import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { WebcamDashboardComponent } from 'app/webcam-dashboard';
import { AuthGuard } from './_guards';
import { LoginComponent } from './login';
import { RegisterComponent } from './register';

const routes: Routes = [
  {path: '', component: WebcamDashboardComponent, canActivate: [AuthGuard]},
  {path: 'login', component: LoginComponent},
  {path: 'webcam', component: WebcamDashboardComponent},
  {path: 'register', component: RegisterComponent},
  {path: '**', redirectTo: ''}
];


@NgModule({
  imports: [RouterModule.forRoot(routes, {useHash: true})],
  exports: [RouterModule]
})
export class AppRoutingModule {
}


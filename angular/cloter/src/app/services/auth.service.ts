import {Injectable} from '@angular/core';
import {JwtHelperService} from "@auth0/angular-jwt";
import {BehaviorSubject, from, Observable, of} from "rxjs";
import {map, switchMap, take} from "rxjs/operators";
import {HttpClient} from '@angular/common/http';
import {Platform} from "@ionic/angular";
import {Router} from "@angular/router";
import { Storage } from '@ionic/storage';


const helper = new JwtHelperService();
const TOKEN_KEY = 'jwt-token';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  URL_AUTH = 'http://localhost/api/token/';
  public user: Observable<any>;
  private userData = new BehaviorSubject(null);

  constructor(private storage: Storage,
              private http: HttpClient,
              private plt: Platform,
              private router: Router) {
    this.loadStoredToken();
  }


  loadStoredToken() {
    let platformObs = from(this.plt.ready());

    this.user = platformObs.pipe(
      switchMap(() => {
        console.log('#########');
        console.log(TOKEN_KEY);
        console.log('#########');
        return from(this.storage.get(TOKEN_KEY));

      }),
      map(token => {
        if (token) {
          console.log('#########');
          console.log(token);
          console.log('#########');
          let decoded = helper.decodeToken(token);
          this.userData.next(decoded);
          return true;
        } else {
          return null;
        }
      })
    );
  }


  login(credentials: any) {

    return this.http.post(this.URL_AUTH, credentials).pipe(
      take(1),
      map(res => {
        // Extract the JWT, here we just fake it
        return res['access'];
      }),
      switchMap(token => {
        let decoded = helper.decodeToken(token);
        this.userData.next(decoded);

        return from(this.storage.set(TOKEN_KEY, token));
      })
    );
  }

  getUser() {
    return this.userData.getValue();
  }

  logout() {
    this.storage.remove(TOKEN_KEY).then(() => {
      this.router.navigateByUrl('/');
      this.userData.next(null);
    });
  }


}


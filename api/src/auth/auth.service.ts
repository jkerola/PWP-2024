import { Injectable, UnauthorizedException } from '@nestjs/common';
import { UsersService } from '../users/users.service';
import * as bcrypt from 'bcrypt';
import { AuthDto } from './dto/auth.dto';
import { TokenDto } from './dto/token.dto';
import { JwtService } from '@nestjs/jwt';
import { RegisterDto } from './dto/registerDto';
import { ProfileDto } from './dto/profile.dto';

@Injectable()
export class AuthService {
  constructor(
    private users: UsersService,
    private jwt: JwtService,
  ) {}

  async signIn(authDto: AuthDto): Promise<TokenDto> {
    const user = await this.users.getUser({
      username: authDto.username,
    });
    if (user != null && (await bcrypt.compare(authDto.password, user.hash))) {
      const payload = { sub: user.id, username: user.username };
      return { token: await this.jwt.signAsync(payload) };
    } else {
      throw new UnauthorizedException();
    }
  }

  async register(registerDto: RegisterDto): Promise<any> {
    const hash = await bcrypt.hash(registerDto.password, 10);
    delete registerDto.password;
    const data = { hash, ...registerDto };
    return this.users.createUser(data);
  }

  async getProfile(userId: string): Promise<ProfileDto> {
    return new ProfileDto(
      await this.users.getUser(
        { id: userId },
        {
          loans: true,
          incidents: true,
        },
      ),
    );
  }
}

import { IsNotEmpty, Length, IsOptional } from 'class-validator';

export class RegisterDto {
  @IsNotEmpty()
  @Length(5, 64)
  username: string;
  @IsNotEmpty()
  @Length(5, 64)
  password: string;

  @IsOptional()
  firstName: string;

  @IsOptional()
  lastName: string;

  @IsOptional()
  address: string;
}

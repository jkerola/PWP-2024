import { User, Loan, Incident } from '@prisma/client';
import { Exclude } from 'class-transformer';

export class ProfileDto implements User {
  @Exclude()
  hash: string;

  id: string;
  username: string;
  firstName: string;
  lastName: string;
  address: string;
  loans: Loan[];
  incidents: Incident[];

  constructor(partial: Partial<ProfileDto>) {
    Object.assign(this, partial);
  }
}
